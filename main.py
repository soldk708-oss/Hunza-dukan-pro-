import streamlit as st
import sqlite3
from datetime import date

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="DukaanPro",
    page_icon="🛒",
    layout="wide"
)

DB_NAME = "dukaanpro.db"


# ==========================================
# RESPONSIVE NAVY BLUE + WHITE THEME
# ==========================================

st.markdown("""
<style>

/* ==========================================
   MAIN APP
   ========================================== */

.stApp {
    background-color: #F4F7FB;
}

h1, h2, h3, h4 {
    color: #0B1F3A !important;
}

h1 {
    font-weight: 800 !important;
}


/* ==========================================
   BUTTONS
   ========================================== */

.stButton > button,
.stFormSubmitButton > button {
    background-color: #0B1F3A !important;
    color: #FFFFFF !important;
    border: 1px solid #0B1F3A !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    width: 100%;
    min-height: 42px;
    white-space: normal !important;
    word-break: break-word;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #163A63 !important;
    border-color: #163A63 !important;
    color: #FFFFFF !important;
}


/* ==========================================
   METRIC CARDS
   ========================================== */

[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #D9E1EC;
    border-left: 5px solid #0B1F3A;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0 2px 8px rgba(11,31,58,0.08);
    min-width: 0 !important;
    overflow: hidden !important;
}

[data-testid="stMetricValue"] {
    color: #0B1F3A !important;
    overflow-wrap: anywhere !important;
}

[data-testid="stMetricLabel"] {
    color: #53657D !important;
    overflow-wrap: anywhere !important;
}


/* ==========================================
   INPUTS
   ========================================== */

.stTextInput input,
.stNumberInput input {
    background-color: #FFFFFF !important;
    color: #172033 !important;
    border: 1px solid #C8D2E0 !important;
    border-radius: 7px !important;
    width: 100% !important;
    box-sizing: border-box !important;
}

div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border-color: #C8D2E0 !important;
    width: 100% !important;
}


/* ==========================================
   TABS
   ========================================== */

.stTabs [data-baseweb="tab-list"] {
    background-color: #FFFFFF;
    border-radius: 9px;
    padding: 6px;
    gap: 5px;
    overflow-x: auto !important;
    scrollbar-width: thin;
}

.stTabs [data-baseweb="tab"] {
    color: #0B1F3A !important;
    font-weight: 600;
    white-space: nowrap !important;
}

.stTabs [aria-selected="true"] {
    background-color: #0B1F3A !important;
    color: #FFFFFF !important;
    border-radius: 7px;
}


/* ==========================================
   EXPANDERS
   ========================================== */

[data-testid="stExpander"] {
    background-color: #FFFFFF;
    border: 1px solid #D9E1EC;
    border-radius: 9px;
    max-width: 100% !important;
    overflow: hidden !important;
}


/* ==========================================
   CONTAINERS
   ========================================== */

[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF;
    border-color: #D9E1EC;
    border-radius: 10px;
    max-width: 100% !important;
    overflow: hidden !important;
}


/* ==========================================
   GENERAL RESPONSIVE SAFETY
   ========================================== */

* {
    box-sizing: border-box;
}

img,
video,
iframe {
    max-width: 100% !important;
}

p,
span,
div,
label {
    overflow-wrap: anywhere;
}


/* ==========================================
   FOOTER
   ========================================== */

.dukaan-footer {
    background-color: #0B1F3A;
    color: #FFFFFF;
    padding: 18px;
    text-align: center;
    border-radius: 10px;
    margin-top: 30px;
    font-weight: 600;
    width: 100%;
    box-sizing: border-box;
    overflow-wrap: anywhere;
}


/* ==========================================
   TABLET
   ========================================== */

@media (max-width: 900px) {

    h1 {
        font-size: 2rem !important;
    }

    h2 {
        font-size: 1.5rem !important;
    }

    h3 {
        font-size: 1.25rem !important;
    }

    [data-testid="stMetric"] {
        padding: 12px;
    }
}


/* ==========================================
   MOBILE
   ========================================== */

@media (max-width: 640px) {

    .block-container {
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    h1 {
        font-size: 1.65rem !important;
        line-height: 1.2 !important;
    }

    h2 {
        font-size: 1.35rem !important;
        line-height: 1.25 !important;
    }

    h3 {
        font-size: 1.15rem !important;
        line-height: 1.3 !important;
    }

    .stCaption {
        font-size: 0.85rem !important;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        min-height: 44px !important;
        font-size: 0.9rem !important;
        padding: 8px 10px !important;
    }

    [data-testid="stMetric"] {
        padding: 11px !important;
        min-height: auto !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.35rem !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.78rem !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        width: 100% !important;
        overflow-x: auto !important;
        flex-wrap: nowrap !important;
    }

    .stTabs [data-baseweb="tab"] {
        min-width: max-content !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
        font-size: 0.85rem !important;
    }

    .stTextInput,
    .stNumberInput,
    .stSelectbox {
        width: 100% !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        width: 100% !important;
        padding: 10px !important;
    }

    .dukaan-footer {
        font-size: 0.85rem !important;
        padding: 14px 10px !important;
    }

    body,
    .stApp {
        overflow-x: hidden !important;
    }
}


/* ==========================================
   VERY SMALL PHONES
   ========================================== */

@media (max-width: 400px) {

    .block-container {
        padding-left: 0.55rem !important;
        padding-right: 0.55rem !important;
    }

    h1 {
        font-size: 1.45rem !important;
    }

    h2 {
        font-size: 1.2rem !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.15rem !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.7rem !important;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        font-size: 0.82rem !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# DATABASE
# ==========================================

def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            udhaar REAL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT,
            sale_date TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT,
            expense_date TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS udhaar_payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TEXT NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_number TEXT UNIQUE,
            customer_name TEXT,
            customer_phone TEXT,
            subtotal REAL,
            discount REAL,
            total REAL,
            bill_date TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bill_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_id INTEGER NOT NULL,
            product_name TEXT,
            quantity REAL,
            price REAL,
            total REAL,
            FOREIGN KEY(bill_id) REFERENCES bills(id)
        )
    """)

    conn.commit()
    conn.close()


create_database()


# ==========================================
# RESET
# ==========================================

def reset_all_data():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM bill_items")
    cursor.execute("DELETE FROM bills")
    cursor.execute("DELETE FROM udhaar_payments")
    cursor.execute("DELETE FROM customers")
    cursor.execute("DELETE FROM sales")
    cursor.execute("DELETE FROM expenses")

    for table in [
        "bill_items",
        "bills",
        "udhaar_payments",
        "customers",
        "sales",
        "expenses"
    ]:
        cursor.execute(
            f"DELETE FROM sqlite_sequence WHERE name='{table}'"
        )

    conn.commit()
    conn.close()


# ==========================================
# HEADER
# ==========================================

header1, header2 = st.columns([5, 1])

with header1:

    st.title("🛒 DukaanPro")

    st.caption("Apni dukaan ka hisaab, ek jagah.")

with header2:

    st.write("")

    if st.button("🔄 Reset", use_container_width=True):

        st.session_state["show_reset_confirm"] = True


if st.session_state.get("show_reset_confirm", False):

    st.warning(
        "⚠️ Customers, Udhaar, Sales, Expenses, Bills "
        "aur History ka poora data clear ho jayega."
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "✅ Haan, Sab Reset Karo",
            use_container_width=True,
            type="primary"
        ):

            reset_all_data()

            st.session_state["show_reset_confirm"] = False

            st.success("✅ DukaanPro reset ho gaya.")

            st.rerun()

    with c2:

        if st.button(
            "❌ Cancel",
            use_container_width=True
        ):

            st.session_state["show_reset_confirm"] = False

            st.rerun()


st.divider()


# ==========================================
# CUSTOMER FUNCTIONS
# ==========================================

def add_customer(name, phone, udhaar):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO customers(name, phone, udhaar)
        VALUES (?, ?, ?)
        """,
        (name, phone, udhaar)
    )

    conn.commit()
    conn.close()


def get_customers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, phone, udhaar
        FROM customers
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_customer(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM udhaar_payments WHERE customer_id=?",
        (customer_id,)
    )

    cursor.execute(
        "DELETE FROM customers WHERE id=?",
        (customer_id,)
    )

    conn.commit()
    conn.close()


def make_udhaar_payment(customer_id, amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT udhaar FROM customers WHERE id=?",
        (customer_id,)
    )

    result = cursor.fetchone()

    if result is None:

        conn.close()

        return False, "Customer nahi mila."

    current_udhaar = float(result[0])

    if amount <= 0:

        conn.close()

        return False, "Amount 0 se zyada hona chahiye."

    if amount > current_udhaar:

        conn.close()

        return False, "Payment current udhaar se zyada nahi ho sakti."

    new_udhaar = current_udhaar - amount

    cursor.execute(
        """
        UPDATE customers
        SET udhaar=?
        WHERE id=?
        """,
        (new_udhaar, customer_id)
    )

    cursor.execute(
        """
        INSERT INTO udhaar_payments
        (customer_id, amount, payment_date)
        VALUES (?, ?, ?)
        """,
        (
            customer_id,
            amount,
            str(date.today())
        )
    )

    conn.commit()
    conn.close()

    return True, new_udhaar


def get_customer_payments(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT amount, payment_date
        FROM udhaar_payments
        WHERE customer_id=?
        ORDER BY id DESC
        """,
        (customer_id,)
    )

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================================
# SALES
# ==========================================

def add_sale(amount, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sales
        (amount, description, sale_date)
        VALUES (?, ?, ?)
        """,
        (
            amount,
            description,
            str(date.today())
        )
    )

    conn.commit()
    conn.close()


def get_today_sales():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(amount),0)
        FROM sales
        WHERE sale_date=?
        """,
        (str(date.today()),)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_sales():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COALESCE(SUM(amount),0) FROM sales"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================================
# EXPENSES
# ==========================================

def add_expense(amount, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses
        (amount, description, expense_date)
        VALUES (?, ?, ?)
        """,
        (
            amount,
            description,
            str(date.today())
        )
    )

    conn.commit()
    conn.close()


def get_today_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(amount),0)
        FROM expenses
        WHERE expense_date=?
        """,
        (str(date.today()),)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COALESCE(SUM(amount),0) FROM expenses"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================================
# BILL FUNCTIONS
# ==========================================

def generate_bill_number():

    today = date.today().strftime("%Y%m%d")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM bills
        WHERE bill_date=?
        """,
        (str(date.today()),)
    )

    count = cursor.fetchone()[0] + 1

    conn.close()

    return f"DP-{today}-{count:03d}"


def save_bill(
    bill_number,
    customer_name,
    customer_phone,
    subtotal,
    discount,
    total,
    items
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bills
        (
            bill_number,
            customer_name,
            customer_phone,
            subtotal,
            discount,
            total,
            bill_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            bill_number,
            customer_name,
            customer_phone,
            subtotal,
            discount,
            total,
            str(date.today())
        )
    )

    bill_id = cursor.lastrowid

    for item in items:

        cursor.execute(
            """
            INSERT INTO bill_items
            (
                bill_id,
                product_name,
                quantity,
                price,
                total
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                bill_id,
                item["name"],
                item["quantity"],
                item["price"],
                item["total"]
            )
        )

    conn.commit()
    conn.close()


def get_bills():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            bill_number,
            customer_name,
            customer_phone,
            subtotal,
            discount,
            total,
            bill_date
        FROM bills
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_bill_items(bill_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            product_name,
            quantity,
            price,
            total
        FROM bill_items
        WHERE bill_id=?
        """,
        (bill_id,)
    )

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================================
# HISTORY
# ==========================================

def get_daily_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            dates.day,
            COALESCE(s.sales,0),
            COALESCE(e.expenses,0)

        FROM
        (
            SELECT sale_date AS day FROM sales
            UNION
            SELECT expense_date AS day FROM expenses
        ) dates

        LEFT JOIN
        (
            SELECT
                sale_date,
                SUM(amount) AS sales
            FROM sales
            GROUP BY sale_date
        ) s
        ON dates.day=s.sale_date

        LEFT JOIN
        (
            SELECT
                expense_date,
                SUM(amount) AS expenses
            FROM expenses
            GROUP BY expense_date
        ) e
        ON dates.day=e.expense_date

        ORDER BY dates.day DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================================
# DASHBOARD
# ==========================================

customers = get_customers()

total_customers = len(customers)

total_udhaar = sum(
    float(customer[3])
    for customer in customers
)

today_sales = get_today_sales()
today_expenses = get_today_expenses()

today_result = today_sales - today_expenses

st.subheader("📊 Today's Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    st.metric(
        "👥 Customers",
        total_customers
    )

with col2:

    st.metric(
        "💰 Today's Sales",
        f"Rs. {today_sales:,.0f}"
    )

with col3:

    st.metric(
        "💸 Today's Expenses",
        f"Rs. {today_expenses:,.0f}"
    )

with col4:

    if today_result >= 0:

        st.metric(
            "📈 Today's Profit",
            f"Rs. {today_result:,.0f}"
        )

    else:

        st.metric(
            "📉 Today's Loss",
            f"Rs. {abs(today_result):,.0f}"
        )

with col5:

    st.metric(
        "💳 Total Udhaar",
        f"Rs. {total_udhaar:,.0f}"
    )


st.divider()


# ==========================================
# TABS
# ==========================================

tab1, tab2, tab3 = st.tabs([
    "🧾 Create Bill",
    "💰 Add Sale",
    "💸 Add Expense"
])


# ==========================================
# CREATE BILL
# ==========================================

with tab1:

    st.subheader("🧾 Create New Bill")

    existing_customers = get_customers()

    customer_options = ["Walk-in Customer"]

    for customer in existing_customers:

        customer_options.append(
            f"{customer[1]} | {customer[2]}"
        )

    selected_customer = st.selectbox(
        "Customer",
        customer_options
    )

    custom_name = ""
    custom_phone = ""

    if selected_customer == "Walk-in Customer":

        c1, c2 = st.columns(2)

        with c1:

            custom_name = st.text_input(
                "Customer Name",
                placeholder="Optional"
            )

        with c2:

            custom_phone = st.text_input(
                "Customer Phone",
                placeholder="Optional"
            )

    else:

        selected_index = customer_options.index(
            selected_customer
        )

        customer_data = existing_customers[
            selected_index - 1
        ]

        custom_name = customer_data[1]
        custom_phone = customer_data[2]

    st.markdown("### 🛍️ Bill Items")

    if "bill_items" not in st.session_state:

        st.session_state.bill_items = []

    c1, c2, c3 = st.columns([3, 1, 2])

    with c1:

        item_name = st.text_input(
            "Item Name",
            placeholder="Example: Shirt"
        )

    with c2:

        item_quantity = st.number_input(
            "Quantity",
            min_value=1.0,
            step=1.0
        )

    with c3:

        item_price = st.number_input(
            "Price",
            min_value=0.0,
            step=100.0
        )

    if st.button(
        "➕ Add Item",
        key="add_bill_item"
    ):

        if item_name.strip() == "":

            st.error("Item ka naam enter karo.")

        elif item_price <= 0:

            st.error("Item price enter karo.")

        else:

            st.session_state.bill_items.append(
                {
                    "name": item_name.strip(),
                    "quantity": item_quantity,
                    "price": item_price,
                    "total": item_quantity * item_price
                }
            )

            st.success("Item bill mein add ho gaya.")

    if st.session_state.bill_items:

        st.markdown("### 📋 Current Bill")

        subtotal = 0

        for index, item in enumerate(
            st.session_state.bill_items
        ):

            subtotal += item["total"]

            c1, c2, c3, c4 = st.columns(
                [4, 1, 2, 1]
            )

            with c1:

                st.write(f"**{item['name']}**")

            with c2:

                st.write(f"{item['quantity']:g}")

            with c3:

                st.write(
                    f"Rs. {item['total']:,.0f}"
                )

            with c4:

                if st.button(
                    "🗑️",
                    key=f"remove_{index}"
                ):

                    st.session_state.bill_items.pop(
                        index
                    )

                    st.rerun()

        discount = st.number_input(
            "Discount",
            min_value=0.0,
            step=100.0,
            key="bill_discount"
        )

        if discount > subtotal:

            discount = subtotal

        grand_total = subtotal - discount

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.write(
                f"### Subtotal: Rs. {subtotal:,.0f}"
            )

            st.write(
                f"### Discount: Rs. {discount:,.0f}"
            )

        with c2:

            st.markdown(
                f"""
                <div style="
                    background-color:#0B1F3A;
                    padding:18px;
                    border-radius:10px;
                    text-align:center;
                    width:100%;
                    box-sizing:border-box;
                    overflow-wrap:anywhere;
                ">
                    <div style="
                        color:#FFFFFF;
                        font-size:18px;
                        font-weight:600;
                    ">
                        Grand Total
                    </div>
                    <div style="
                        color:#FFFFFF;
                        font-size:28px;
                        font-weight:800;
                    ">
                        Rs. {grand_total:,.0f}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        if st.button(
            "🧾 Generate & Save Bill",
            use_container_width=True,
            type="primary"
        ):

            bill_number = generate_bill_number()

            save_bill(
                bill_number,
                custom_name,
                custom_phone,
                subtotal,
                discount,
                grand_total,
                st.session_state.bill_items
            )

            item_names = ", ".join(
                item["name"]
                for item in st.session_state.bill_items
            )

            add_sale(
                grand_total,
                f"Bill {bill_number}: {item_names}"
            )

            st.session_state.last_bill = {
                "bill_number": bill_number,
                "customer_name": custom_name,
                "customer_phone": custom_phone,
                "items": st.session_state.bill_items.copy(),
                "subtotal": subtotal,
                "discount": discount,
                "total": grand_total
            }

            st.session_state.bill_items = []

            st.success(
                f"✅ Bill {bill_number} save ho gaya!"
            )

            st.rerun()


# ==========================================
# RECEIPT
# ==========================================

if st.session_state.get("last_bill"):

    bill = st.session_state.last_bill

    st.divider()

    st.subheader("🧾 Generated Receipt")

    st.markdown(
        f"""
        <div style="
            background-color:#FFFFFF;
            border:2px solid #0B1F3A;
            border-radius:12px;
            padding:22px;
            width:100%;
            box-sizing:border-box;
            overflow-wrap:anywhere;
        ">

        <h2 style="
            color:#0B1F3A !important;
        ">
            🛒 DukaanPro
        </h2>

        <p>
            <b>Bill:</b> {bill['bill_number']}
        </p>

        <p>
            <b>Customer:</b>
            {bill['customer_name'] or 'Walk-in Customer'}
        </p>

        <p>
            <b>Phone:</b>
            {bill['customer_phone'] or 'N/A'}
        </p>

        <hr>
        """,
        unsafe_allow_html=True
    )

    for item in bill["items"]:

        st.write(
            f"**{item['name']}** — "
            f"{item['quantity']:g} × "
            f"Rs. {item['price']:,.0f} = "
            f"Rs. {item['total']:,.0f}"
        )

    st.markdown(
        f"""
        <hr>

        <p>
            <b>Subtotal:</b>
            Rs. {bill['subtotal']:,.0f}
        </p>

        <p>
            <b>Discount:</b>
            Rs. {bill['discount']:,.0f}
        </p>

        <h2 style="
            color:#0B1F3A !important;
            overflow-wrap:anywhere;
        ">
            Grand Total:
            Rs. {bill['total']:,.0f}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# BILL HISTORY
# ==========================================

st.divider()

st.subheader("📜 Bill History")

bills = get_bills()

if bills:

    for bill in bills:

        (
            bill_id,
            bill_number,
            customer_name,
            customer_phone,
            subtotal,
            discount,
            total,
            bill_date
        ) = bill

        with st.expander(
            f"🧾 {bill_number} — "
            f"Rs. {total:,.0f} — {bill_date}"
        ):

            st.write(
                f"**Customer:** "
                f"{customer_name or 'Walk-in Customer'}"
            )

            st.write(
                f"**Phone:** "
                f"{customer_phone or 'N/A'}"
            )

            items = get_bill_items(bill_id)

            for item in items:

                product_name, quantity, price, item_total = item

                st.write(
                    f"• {product_name} — "
                    f"{quantity:g} × "
                    f"Rs. {price:,.0f} = "
                    f"Rs. {item_total:,.0f}"
                )

            st.divider()

            st.write(
                f"Subtotal: Rs. {subtotal:,.0f}"
            )

            st.write(
                f"Discount: Rs. {discount:,.0f}"
            )

            st.markdown(
                f"### Total: Rs. {total:,.0f}"
            )


# ==========================================
# ADD SALE
# ==========================================

with tab2:

    st.subheader("💰 Add New Sale")

    with st.form("sale_form"):

        sale_amount = st.number_input(
            "Sale Amount",
            min_value=0.0,
            step=100.0
        )

        sale_description = st.text_input(
            "Description",
            placeholder="Example: 2 shirts"
        )

        submit_sale = st.form_submit_button(
            "➕ Add Sale"
        )

        if submit_sale:

            if sale_amount <= 0:

                st.error("Sale amount enter karo.")

            else:

                add_sale(
                    sale_amount,
                    sale_description
                )

                st.success(
                    f"Sale Rs. {sale_amount:,.0f} add ho gayi!"
                )

                st.rerun()


# ==========================================
# ADD EXPENSE
# ==========================================

with tab3:

    st.subheader("💸 Add New Expense")

    with st.form("expense_form"):

        expense_amount = st.number_input(
            "Expense Amount",
            min_value=0.0,
            step=100.0
        )

        expense_description = st.text_input(
            "Description",
            placeholder="Example: Electricity"
        )

        submit_expense = st.form_submit_button(
            "➕ Add Expense"
        )

        if submit_expense:

            if expense_amount <= 0:

                st.error("Expense amount enter karo.")

            else:

                add_expense(
                    expense_amount,
                    expense_description
                )

                st.success(
                    f"Expense Rs. {expense_amount:,.0f} add ho gayi!"
                )

                st.rerun()


# ==========================================
# HISTORY
# ==========================================

st.divider()

st.header("📅 Hisab History")

history = get_daily_history()

if history:

    for day, sales, expenses in history:

        result = sales - expenses

        st.subheader(f"📅 {day}")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "💰 Sales",
                f"Rs. {sales:,.0f}"
            )

        with c2:

            st.metric(
                "💸 Expenses",
                f"Rs. {expenses:,.0f}"
            )

        with c3:

            if result >= 0:

                st.metric(
                    "📈 Profit",
                    f"Rs. {result:,.0f}"
                )

            else:

                st.metric(
                    "📉 Loss",
                    f"Rs. {abs(result):,.0f}"
                )

        st.divider()

    st.subheader("📊 Overall Business Summary")

    total_sales = get_total_sales()
    total_expenses = get_total_expenses()

    total_result = total_sales - total_expenses

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "💰 Total Sales",
            f"Rs. {total_sales:,.0f}"
        )

    with c2:

        st.metric(
            "💸 Total Expenses",
            f"Rs. {total_expenses:,.0f}"
        )

    with c3:

        if total_result >= 0:

            st.metric(
                "📈 Total Profit",
                f"Rs. {total_result:,.0f}"
            )

        else:

            st.metric(
                "📉 Total Loss",
                f"Rs. {abs(total_result):,.0f}"
            )

else:

    st.info(
        "Abhi koi sales ya expenses ka record nahi hai."
    )


# ==========================================
# CUSTOMERS
# ==========================================

st.divider()

st.header("👤 Customers")

with st.form("customer_form"):

    c1, c2, c3 = st.columns(3)

    with c1:

        name = st.text_input(
            "Customer Name",
            placeholder="Example: Ali"
        )

    with c2:

        phone = st.text_input(
            "Phone Number",
            placeholder="03XXXXXXXXX"
        )

    with c3:

        udhaar = st.number_input(
            "Udhaar Amount",
            min_value=0.0,
            step=100.0
        )

    submit_customer = st.form_submit_button(
        "➕ Add Customer"
    )

    if submit_customer:

        if name.strip() == "":

            st.error(
                "Customer ka naam enter karo."
            )

        else:

            add_customer(
                name.strip(),
                phone.strip(),
                udhaar
            )

            st.success(
                f"✅ {name} successfully add ho gaya!"
            )

            st.rerun()


# ==========================================
# CUSTOMER SEARCH
# ==========================================

st.subheader("🔎 Customer Search")

search_text = st.text_input(
    "Naam ya phone number se search karo",
    placeholder="Example: Ali ya 0300"
)

customers = get_customers()

if search_text.strip():

    search_lower = search_text.strip().lower()

    customers = [
        customer
        for customer in customers
        if search_lower in str(customer[1]).lower()
        or search_lower in str(customer[2]).lower()
    ]


# ==========================================
# CUSTOMER LIST
# ==========================================

if customers:

    for customer in customers:

        customer_id = customer[0]
        customer_name = customer[1]
        customer_phone = customer[2]
        customer_udhaar = float(customer[3])

        with st.container(border=True):

            c1, c2, c3, c4 = st.columns(
                [2, 2, 2, 1]
            )

            with c1:

                st.write(
                    f"**👤 {customer_name}**"
                )

            with c2:

                st.write(
                    f"📱 {customer_phone or 'No phone'}"
                )

            with c3:

                st.write(
                    f"💳 Udhaar: "
                    f"Rs. {customer_udhaar:,.0f}"
                )

            with c4:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{customer_id}"
                ):

                    delete_customer(
                        customer_id
                    )

                    st.rerun()

            if customer_udhaar > 0:

                st.markdown(
                    "**💵 Udhaar Payment**"
                )

                c1, c2 = st.columns([3, 1])

                with c1:

                    payment_amount = st.number_input(
                        "Wapas ki gayi amount",
                        min_value=0.0,
                        max_value=customer_udhaar,
                        step=100.0,
                        key=f"payment_{customer_id}"
                    )

                with c2:

                    st.write("")
                    st.write("")

                    if st.button(
                        "💵 Payment Add",
                        key=f"pay_{customer_id}"
                    ):

                        success, result = make_udhaar_payment(
                            customer_id,
                            payment_amount
                        )

                        if success:

                            st.success(
                                f"Rs. {payment_amount:,.0f} "
                                f"receive ho gaye. "
                                f"Remaining udhaar: "
                                f"Rs. {result:,.0f}"
                            )

                            st.rerun()

                        else:

                            st.error(result)

            else:

                st.success(
                    "✅ Is customer ka koi udhaar nahi hai."
                )

            payments = get_customer_payments(
                customer_id
            )

            if payments:

                with st.expander(
                    "📜 Udhaar Payment History"
                ):

                    for amount, payment_date in payments:

                        st.write(
                            f"📅 {payment_date} — "
                            f"💵 Rs. {amount:,.0f}"
                        )

else:

    if search_text.strip():

        st.info(
            "Is search ke mutabiq koi customer nahi mila."
        )

    else:

        st.info(
            "Abhi koi customer add nahi hua."
        )


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="dukaan-footer">
        DukaanPro 🚀 | Business Management Software
    </div>
    """,
    unsafe_allow_html=True
)