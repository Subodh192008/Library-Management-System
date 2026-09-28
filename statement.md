Updated problem statement and scope document for your project report.

```markdown
## Problem Statement & Scope

# 1. Problem Statement
In traditional college reading rooms and departmental libraries, students borrow textbooks and reference manuals by manually signing a physical register. This conventional method presents several bottlenecks:
- Entries are frequently illegible or omitted, leading to unaccounted or missing books.
- Certain students hoard multiple reference copies at once, depriving others of vital study resources.
- Library staff have to physically inspect shelves to determine which high-demand titles need to be restocked.

# 2. Project Scope
This project is an entry-level command-line application designed to replace the paper register at the library issue counter. It provides real-time stock visibility, tracks active loans by student registration numbers, enforces a 2-book maximum holding limit, and issues immediate alerts when textbook stocks run low.

# 3. Target Users
- **Students:** To quickly check the availability of specific textbooks and borrow resources equitably.
- **Librarians / Library Staff:** To process issues and returns smoothly, track outstanding books, and monitor replenishment needs.

# 4. Key Features
- **Real-Time Stock Tracking:** Catalog copies decrease by 1 upon issue and increase by 1 upon return.
- **Borrowing Cap (Max 2 Books):** Prevents hoarding by restricting active loans to 2 per student registration number.
- **Loan Tracking:** Maintains a running list of `(student_reg, book_title)` pairs.
- **Low Stock Notifications:** Warns staff whenever the available count for any title falls below 2 copies.
