# =============================================================================
# ACCESS MODIFIERS IN PYTHON
# =============================================================================
# Python doesn't enforce access control the way Java/C++ does.
# Instead it uses naming conventions that communicate INTENT.
# The mantra: "We're all consenting adults here."
# =============================================================================

# =============================================================================
# SECTION 1: Public Members (the default)
# =============================================================================
print("=" * 60)
print("SECTION 1: Public Members")
print("=" * 60)

class UserAccount:
    def __init__(self, username: str, email: str):
        self.username = username   # public — readable and writable by anyone
        self.email = email         # public

    def display(self):
        print(f"User: {self.username} | Email: {self.email}")

user = UserAccount("alice", "alice@example.com")
user.display()

# Anyone can read AND overwrite public fields — no restriction at all
user.email = "hacker@evil.com"
print(f"Email after external change: {user.email}")

# =============================================================================
# SECTION 2: Protected Members (single underscore _)
# =============================================================================
print("\n" + "=" * 60)
print("SECTION 2: Protected Members (single underscore _)")
print("=" * 60)

# Senior tip: A single underscore is a social contract, not a lock.
# It means "internal use — touch this and you own the consequences."
# Python will NOT stop you, but linters and code reviewers will notice.

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = balance        # "protected" — internal use / subclasses
        self._transaction_history = [] # same — callers shouldn't poke this directly

    def deposit(self, amount: float):
        self._balance += amount
        self._transaction_history.append(f"+{amount}")

    def get_balance(self):
        return self._balance

class PremiumBankAccount(BankAccount):
    def __init__(self, owner: str, balance: float, credit_limit: float):
        super().__init__(owner, balance)
        self._credit_limit = credit_limit

    def withdraw(self, amount: float):
        # Subclass accessing _balance is the intended use of protected
        if amount <= self._balance + self._credit_limit:
            self._balance -= amount
            self._transaction_history.append(f"-{amount}")
        else:
            print("Insufficient funds + credit")

account = PremiumBankAccount("Bob", 1000.0, 500.0)
account.deposit(200)
account.withdraw(300)
print(f"Balance: {account.get_balance()}")

# You CAN still access _balance from outside — Python won't stop you.
# Senior tip: Don't do this in production code. It breaks encapsulation
# and you'll be debugging why the balance is wrong at 2am.
print(f"Direct access still works (don't do this): {account._balance}")

# =============================================================================
# SECTION 3: Private Members (double underscore __ — name mangling)
# =============================================================================
print("\n" + "=" * 60)
print("SECTION 3: Private Members (double underscore __)")
print("=" * 60)

# Senior tip: Double underscore triggers Python's NAME MANGLING.
# __attr becomes _ClassName__attr. This is the only real enforcement Python
# does — and its purpose is to avoid accidental collisions in subclasses,
# NOT to be a security wall. A determined caller can still reach it.

class PaymentProcessor:
    def __init__(self, api_key: str):
        self.__api_key = api_key   # name-mangled to _PaymentProcessor__api_key
        self.__secret_salt = "x7k2"

    def charge(self, amount: float, card_token: str):
        signature = self.__build_signature(card_token)
        print(f"Charging ${amount} | signature={signature[:8]}...")

    def __build_signature(self, card_token: str):
        # Private helper — callers have no business calling this directly
        return f"{card_token}{self.__secret_salt}{self.__api_key}"

processor = PaymentProcessor("sk_live_abc123")
processor.charge(49.99, "tok_visa")

# Trying to access __api_key directly raises AttributeError
try:
    print(processor.__api_key)
except AttributeError as e:
    print(f"Direct access blocked: {e}")

# Senior tip: Name mangling is Python being helpful, not a security feature.
# The key is STILL accessible via the mangled name — never store real secrets
# in class attributes; use env vars or secret managers instead.
# Senior tip: getattr bypasses Pyright's static check but the mangled name is real at runtime.
mangled_key = getattr(processor, "_PaymentProcessor__api_key")
print(f"Mangled name still reachable: {mangled_key[:10]}...")

# =============================================================================
# SECTION 4: Why name mangling exists — subclass collision prevention
# =============================================================================
print("\n" + "=" * 60)
print("SECTION 4: Why __ exists — subclass collision prevention")
print("=" * 60)

# Senior tip: This is the REAL reason for __. Without it, a subclass that
# accidentally reuses a parent's internal attribute name would silently corrupt
# the parent's logic. Name mangling scopes the attribute to its defining class.

class BaseWidget:
    def __init__(self):
        self.__id = "base-widget-001"   # becomes _BaseWidget__id

    def get_id(self):
        return self.__id                # always reads _BaseWidget__id

class FancyWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.__id = "fancy-widget-002"  # becomes _FancyWidget__id — different slot!

    def get_fancy_id(self):
        return self.__id

widget = FancyWidget()
print(f"BaseWidget id (via get_id):        {widget.get_id()}")
print(f"FancyWidget id (via get_fancy_id): {widget.get_fancy_id()}")
# Both coexist peacefully — no silent overwrite

# =============================================================================
# SECTION 5: The Pythonic way — @property for controlled access
# =============================================================================
print("\n" + "=" * 60)
print("SECTION 5: @property — controlled access without Java-style getters")
print("=" * 60)

# Senior tip: Never write get_X() / set_X() methods in Python. Use @property.
# It lets you start with a plain attribute and add validation later WITHOUT
# changing the public API. That's the real superpower.

class OrderItem:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self._price = price
        self._quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    @property
    def total(self) -> float:
        # Read-only computed property — no setter needed
        return self._price * self._quantity

item = OrderItem("Laptop", 999.99, 2)
print(f"Item: {item.name} | Total: ${item.total:.2f}")

item.quantity = 3
print(f"Updated total: ${item.total:.2f}")

# Validation fires on assignment — clean API, no get/set ceremony
try:
    item.price = -50
except ValueError as e:
    print(f"Validation caught: {e}")

# Senior tip: total has no setter, so assigning raises AttributeError cleanly.
# Using setattr() here because direct assignment (`item.total = 9999`) is a
# static type error — Pyright catches it at analysis time, which is correct
# and exactly what you want in a typed codebase.
try:
    setattr(item, "total", 9999)
except AttributeError as e:
    print(f"Read-only property protected: {e}")

# =============================================================================
# SECTION 6: Real-world pattern — combining all three levels
# =============================================================================
print("\n" + "=" * 60)
print("SECTION 6: Real-world pattern — all three levels together")
print("=" * 60)

import hashlib

class UserService:
    """
    Public  : username, email, is_active  — callers read/write freely
    Protected: _role                      — subclasses may extend auth logic
    Private : __password_hash             — no external access ever
    """

    def __init__(self, username: str, email: str, password: str):
        self.username = username          # public
        self.email = email                # public
        self.is_active = True             # public flag
        self._role = "viewer"             # protected — subclasses set roles
        self.__password_hash = self.__hash(password)  # private

    def __hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, candidate: str) -> bool:
        return self.__password_hash == self.__hash(candidate)

    @property
    def role(self) -> str:
        return self._role

class AdminUserService(UserService):
    def __init__(self, username: str, email: str, password: str):
        super().__init__(username, email, password)
        self._role = "admin"   # subclass sets protected _role — intended use

svc = AdminUserService("carol", "carol@company.com", "s3cr3t!")
print(f"User: {svc.username} | Role: {svc.role} | Active: {svc.is_active}")
print(f"Password correct: {svc.verify_password('s3cr3t!')}")
print(f"Wrong password:   {svc.verify_password('wrong')}")

# The hash is never reachable without name mangling — good
try:
    print(svc.__password_hash)
except AttributeError as e:
    print(f"Hash inaccessible: {e}")

print("\n" + "=" * 60)
print("SUMMARY: Python Access Modifier Conventions")
print("=" * 60)
print("  name      -> Public   : no restriction, full API surface")
print("  _name     -> Protected: 'please don't touch' — convention only")
print("  __name    -> Private  : name-mangled, prevents subclass collision")
print("  @property -> Pythonic : validation + computed attrs, no get/set noise")
print("=" * 60)
