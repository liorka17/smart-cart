products = {
    "Milk": 5.90,
    "Bread": 3.50,
    "Eggs": 10.00,
    "Cheese": 12.30,
    "Apple": 2.20,
    "Banana": 3.10,
    "Chicken": 26.90,
    "Rice": 7.80,
    "Tomato": 4.50,
    "Cucumber": 3.80,
    "Yogurt": 4.20,
    "Coffee": 18.00,
    "Sugar": 6.50,
    "Water Bottle": 2.90,
    "Chocolate": 8.40
}

# עגלת קניות – מילון ריק שמתמלא לאורך הקנייה
cart = {}

# פונקציה להצגת כל המוצרים הזמינים בחנות
def show_products():
    print("Available products:")  # כותרת
    for name in products:        # מעבר על כל מוצר במילון
        print(f"{name} - ${products[name]}")  # הדפסת שם המוצר והמחיר שלו

# פונקציה להוספת מוצרים לעגלה
def add_to_cart():
    print("Add products to cart (type 'done' to finish):")  # הנחיה למשתמש
    while True:  # לולאה שרצה עד שהמשתמש כותב "done"
        name_input = input("Enter product name (or 'done' to finish): ")  # קלט שם מוצר
        if name_input.lower() == "done":  # אם המשתמש כתב done
            break  # יציאה מהלולאה
        matched_product = None  # משתנה שיאחסן את שם המוצר שנמצא
        for name in products:  # מעבר על כל המוצרים
            if name_input.lower() == name.lower():  # השוואת שמות בלי תלות באותיות גדולות או קטנות
                matched_product = name  # שמירת השם המקורי מהמילון
                break  # יציאה מהלולאה
        if matched_product is not None:  # אם נמצא מוצר
            quantity_input = input("Enter quantity: ")  # קלט כמות
            if quantity_input.isdigit():  # בדיקה שהכמות היא מספר שלם
                quantity = int(quantity_input)  # המרה למספר
                if matched_product in cart:  # אם המוצר כבר בעגלה
                    cart[matched_product]["quantity"] += quantity  # הוספת כמות
                else:  # אם המוצר לא קיים בעגלה
                    cart[matched_product] = {  # יצירת ערך חדש בעגלה
                        "quantity": quantity,  # שמירת כמות
                        "price": products[matched_product]  # שמירת מחיר
                    }
                print(f"{quantity} x {matched_product} added to cart.")  # הודעה על ההוספה
            else:
                print("Invalid quantity.")  # אם הכמות לא חוקית
        else:
            print("Product not found.")  # אם לא נמצא מוצר מתאים

# פונקציה להסרת מוצר מהעגלה
def remove_from_cart():
    name = input("Enter product name to remove: ")  # קלט שם מוצר להסרה
    for item in cart:  # מעבר על המוצרים בעגלה
        if name.lower() == item.lower():  # אם שם תואם (בלי תלות באותיות גדולות או קטנות)
            del cart[item]  # מחיקה מהמילון
            print("Product removed from cart.")  # הודעה
            return  # יציאה מהפונקציה
    print("Product not found in cart.")  # אם לא נמצא

# פונקציה לחיפוש מוצר בעגלה לפי מחרוזת חלקית
def search_in_cart():
    keyword = input("Enter product name to search: ")  # קלט לחיפוש
    found = False  # דגל למציאה
    for name in cart:  # מעבר על כל פריט בעגלה
        if keyword.lower() in name.lower():  # אם המילה קיימת בשם
            q = cart[name]["quantity"]  # שליפת כמות
            p = cart[name]["price"]     # שליפת מחיר
            print(f"{name} - Quantity: {q}, Price: ${p}")  # הדפסה
            found = True  # שינוי הדגל
    if found == False:  # אם לא נמצא שום דבר
        print("No matching product found in cart.")  # הודעה מתאימה

# פונקציה להצגת כל העגלה כולל סיכום
def show_cart():
    if len(cart) == 0:  # בדיקה אם העגלה ריקה
        print("Cart is empty.")  # הודעה
        return  # סיום הפונקציה
    total = 0  # סכום כולל
    count = 0  # כמות כללית
    print("Cart contents:")  # כותרת
    for name in cart:  # מעבר על כל מוצר בעגלה
        q = cart[name]["quantity"]  # שליפת כמות
        p = cart[name]["price"]     # שליפת מחיר
        print(f"{name} - Quantity: {q} - Price: ${p}")  # הדפסה
        total += q * p  # חישוב סכום מצטבר
        count += q      # חישוב כמות מצטברת
    print("Total items:", count)  # סה"כ פריטים
    print("Total price: $", round(total, 2))  # סה"כ מחיר עם עיגול ל-2 ספרות

# פונקציה לסיום קנייה – Checkout
def checkout():
    show_cart()  # הצגת העגלה
    confirm = input("Confirm checkout? (yes/no): ")  # אישור קנייה
    if confirm.lower() == "yes":  # אם המשתמש אישר
        cart.clear()  # ניקוי העגלה
        print("Checkout complete.")  # הודעה על סיום
