# ייבוא של הפונקציות מקובץ functions.py
from functions import (
    show_products,      # פונקציה שמציגה את כל המוצרים הקיימים
    add_to_cart,        # פונקציה להוספת מוצר לעגלה
    remove_from_cart,   # פונקציה להסרת מוצר מהעגלה
    search_in_cart,     # פונקציה לחיפוש מוצר בעגלה לפי מחרוזת
    show_cart,          # פונקציה שמציגה את כל תוכן העגלה
    checkout            # פונקציה שמסיימת את הקנייה ומנקה את העגלה
)

# הגדרה של פונקציה שמריצה את התפריט הראשי
def menu():
    while True:  # לולאה שרצה כל עוד לא בחרנו לצאת מהתוכנית
        print("===== MAIN MENU =====")                      # הדפסת כותרת התפריט
        print("1. Show available products")                # אפשרות 1 – הצגת מוצרים
        print("2. Add product to cart")                    # אפשרות 2 – הוספת מוצר לעגלה
        print("3. Remove product from cart")               # אפשרות 3 – הסרת מוצר מהעגלה
        print("4. Search product in cart")                 # אפשרות 4 – חיפוש בעגלה
        print("5. Show cart")                              # אפשרות 5 – הצגת העגלה
        print("6. Checkout (finish shopping)")            # אפשרות 6 – סיום קנייה
        print("7. Exit")                                   # אפשרות 7 – יציאה מהתפריט

        choice = input("Enter your choice (1-7): ")       # קבלת קלט מהמשתמש עבור הבחירה בתפריט

        if choice == "1":          # אם המשתמש בחר 1
            show_products()        # קורא לפונקציה שמציגה מוצרים
        elif choice == "2":        # אם המשתמש בחר 2
            add_to_cart()          # קורא לפונקציה שמוסיפה לעגלה
        elif choice == "3":        # אם המשתמש בחר 3
            remove_from_cart()     # קורא לפונקציה שמסירה מוצר מהעגלה
        elif choice == "4":        # אם המשתמש בחר 4
            search_in_cart()       # קורא לפונקציית חיפוש מוצר
        elif choice == "5":        # אם המשתמש בחר 5
            show_cart()            # קורא לפונקציה שמציגה את העגלה
        elif choice == "6":        # אם המשתמש בחר 6
            checkout()             # קורא לפונקציה שמסיימת את הקנייה
        elif choice == "7":        # אם המשתמש בחר 7
            print("Goodbye!")      # הדפסת הודעת יציאה
            break                  # יציאה מהלולאה
        else:                      # אם המשתמש הקליד ערך לא חוקי
            print("Invalid choice.")  # הדפסת הודעה על שגיאה בבחירה

# הפעלת התפריט בפועל
menu()  # קריאה לפונקציה שמציגה את התפריט ומטפלת בבחירת המשתמש
