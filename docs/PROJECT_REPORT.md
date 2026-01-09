# MINI PROJECT REPORT ON
**"Domino Disruption Predictor (DDP)"**

**SUBMITTED BY**
[Your Name]

**UNDER THE GUIDANCE OF**
[Professor Name]

**IN PARTIAL FULFILLMENT OF**
Award of the Degree of
**MASTER OF COMPUTER APPLICATION**
(Semester-I)

**SUBMITTED TO**
[University Name]

**THROUGH**
[Institute Name]
[City]

**ACADEMIC YEAR 2025-2026**

---

# INDEX

| Sr. No. | Topic | Page No. |
| :--- | :--- | :--- |
| 1 | **Introduction** | |
| 1.1 | Introduction | 1 |
| 1.2 | About Existing System | 2 |
| 1.3 | Limitations of the System | 3 |
| 1.4 | Need of System | 4 |
| 1.5 | Hardware Specifications | 5 |
| 1.6 | Software Specifications | 5 |
| 1.7 | Business Objectives | 6 |
| 1.8 | System Objectives | 7 |
| 1.9 | Scope of Program | 8 |
| | | |
| 2 | **System Requirement Specification** | 9 |
| | | |
| 3 | **Design** | |
| 3.1 | Entity Relationship Diagram | 10 |
| 3.2 | Class Diagram | 11 |
| 3.3 | Activity Diagram | 12 |
| 3.4 | Sequence Diagram | 13 |
| 3.5 | Use Case Diagram | 14 |
| | | |
| 4 | **Screenshots** | 15 |
| | | |
| 5 | **Data Dictionary** | 18 |
| | | |
| 6 | **Code Implementation** | 20 |
| | | |
| 7 | **Conclusion** | 40 |
| | | |
| 8 | **Bibliography and References** | 41 |

---

# 1. Introduction

## 1.1 Introduction
In the modern fast-paced world, productivity is often hindered by small, seemingly insignificant interruptions—what we call "domino disruptions." A single distraction, like a notification or a brief chat, can derail focus for hours. The **Domino Disruption Predictor (DDP)** is a web-based application designed to help individuals and organizations track, analyze, and predict these productivity disruptions. By logging disruption events and their causes, users can identify patterns (e.g., "I always get distracted by emails at 10 AM") and receive AI-driven suggestions to prevent them.

The system allows users to log disruptions with details like timestamp, duration, tag (context), and severity. It then visualizes this data through an interactive dashboard, offering insights into total downtime, frequency of disruptions, and root cause analysis.

## 1.2 About Existing System
Currently, most people track their productivity using manual methods:
1.  **Mental Notes:** Trying to remember why they were unproductive.
2.  **Paper Journals:** Writing down distractions in a diary.
3.  **Spreadsheets:** Manually entering data into Excel.

These methods are:
*   **Reactive:** They only look backward, not forward.
*   **Tedious:** Manual entry is boring and often skipped.
*   **Unstructured:** Hard to see patterns without manual calculation.
*   **No Intelligence:** A spreadsheet cannot suggest *solutions* to your problems.

## 1.3 Limitations of the System
While DDP is a robust tool, the current version has some limitations:
1.  **Self-Reporting:** It relies on the user honestly and accurately logging disruptions.
2.  **No Automatic Tracking:** It does not currently monitor computer activity (like screen time) automatically.
3.  **Internet Connection:** As a web app, it requires an internet connection to function.
4.  **Single User Focus:** The current version is optimized for individual use rather than team-wide analytics.

## 1.4 Need of System
1.  **Awareness:** You cannot fix what you cannot measure. DDP makes invisible time-wasters visible.
2.  **Pattern Recognition:** Identifies that 20% of causes leading to 80% of lost time (Pareto Principle).
3.  **Behavioral Change:** By receiving "Root Cause Suggestions," users are nudged toward better habits.
4.  **Data Visualization:** Graphs and charts make it easy to digest complex productivity data instantly.

## 1.5 Hardware Specifications
*   **Processor:** Intel Core i3 or equivalent (Minimum)
*   **RAM:** 4 GB or higher
*   **Hard Disk:** 256 GB SSD (Recommended)
*   **Monitor:** Standard HD Display

## 1.6 Software Specifications
*   **Operating System:** Windows 10/11, macOS, or Linux
*   **Backend Framework:** Python (Django 5.0)
*   **Frontend Technologies:** HTML5, CSS3, JavaScript (Chart.js)
*   **Database:** SQLite (Development) / PostgreSQL (Production)
*   **IDE:** VS Code / PyCharm
*   **Browser:** Chrome / Edge / Firefox

## 1.7 Business Objectives
1.  **Maximize Productivity:** Reduce "downtime" for users.
2.  **Data-Driven Decisions:** Replace gut feelings about productivity with hard data.
3.  **User Retention:** Create a sticky habit of daily logging through a gamified interface.

## 1.8 System Objectives
1.  **Secure Authentication:** Ensure user data is private and secure.
2.  **Fast Logging:** Minimize the friction of logging a disruption (under 5 seconds).
3.  **Real-Time Analytics:** Dashboard updates instantly as new data comes in.
4.  **Responsiveness:** Works seamlessly on desktop and mobile devices.

## 1.9 Scope of Program
The scope of DDP includes:
*   **User Module:** Registration, Login, Profile Management.
*   **Tracking Module:** Logging disruptions with tags, duration, and notes.
*   **Analytics Module:** Dashboard with pie charts (Tag distribution) and line graphs (Daily trends).
*   **Prediction Module:** Simple rule-based engine to suggest fixes (e.g., IF tag="Tech" THEN suggest="Check cables").

---

# 2. System Requirement Specification (SRS)

## 2.1 Functional Requirements
1.  **User Registration:** Users must be able to create an account.
2.  **Login/Logout:** Secure JWT-based authentication.
3.  **Log Disruption:** Form to input time, duration, tag, and context.
4.  **View Dashboard:** Display total stats and charts.
5.  **View History:** List of past disruptions.

## 2.2 Non-Functional Requirements
1.  **Performance:** Page load time under 2 seconds.
2.  **Scalability:** Database design supports thousands of records.
3.  **Usability:** Intuitive UI requiring no training.
4.  **Availability:** 99.9% uptime target.

---

# 3. Design

## 3.1 Entity Relationship Diagram (ERD)
*(Draw a diagram with the following entities)*

*   **User Table:** `id`, `username`, `password`, `email`
*   **Tag Table:** `id`, `name` (e.g., "Tech", "Health")
*   **Disruption Table:** `id`, `user_id` (FK), `tag_id` (FK), `timestamp`, `duration`, `context`, `severity`
*   **RootCauseRule Table:** `id`, `tag_id` (FK), `keyword`, `suggestion`

**Relationships:**
*   One **User** has Many **Disruptions**.
*   One **Tag** has Many **Disruptions**.
*   One **Tag** has Many **RootCauseRules**.

## 3.2 Class Diagram
*(Draw boxes for these classes)*

*   **Class: Disruption**
    *   Attributes: `timestamp`, `duration`, `context`
    *   Methods: `save()`, `calculate_severity()`
*   **Class: User**
    *   Attributes: `username`, `email`
    *   Methods: `login()`, `register()`
*   **Class: DashboardView**
    *   Methods: `get_stats()`, `render_charts()`

## 3.3 Activity Diagram (Log Entry Flow)
1.  Start
2.  User clicks "Log Disruption"
3.  System checks "Is Logged In?"
    *   No -> Redirect to Login
    *   Yes -> Show Form
4.  User fills form (Time, Tag, Context)
5.  User clicks Submit
6.  System validates data
    *   Invalid -> Show Error
    *   Valid -> Save to DB
7.  System checks for Root Cause Suggestions
8.  System displays Success Message + Suggestion
9.  End

---

# 4. Screenshots

## 4.1 Login Page
*(Paste screenshot of login.html here)*
*Description: The secure entry point for the application.*

## 4.2 Dashboard
*(Paste screenshot of dashboard.html here)*
*Description: The central hub showing Total Disruptions, Downtime, and graphical analytics.*

## 4.3 Log Entry Form
*(Paste screenshot of log_entry.html here)*
*Description: The interface for recording a new disruption event.*

---

# 5. Data Dictionary

**Table 1: User**
| Field | Type | Description |
| :--- | :--- | :--- |
| id | Integer | Primary Key |
| username | Varchar(150) | Unique identifier |
| email | Varchar(254) | User email |
| password | Varchar(128) | Hashed password |

**Table 2: Disruption**
| Field | Type | Description |
| :--- | :--- | :--- |
| id | Integer | Primary Key |
| user | ForeignKey | Link to User table |
| tag | ForeignKey | Link to Tag table |
| timestamp | DateTime | When it happened |
| duration | Integer | Duration in minutes |
| context | Text | Optional notes |

---

# 6. Code Implementation

## 6.1 Backend (Django Views)
**File: `core/views.py`**
```python
class DisruptionViewSet(viewsets.ModelViewSet):
    serializer_class = DisruptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Disruption.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Auto-detect root cause
        instance = serializer.save(user=self.request.user)
        suggestion = check_root_cause(instance)
        # ... logic to return suggestion
```

## 6.2 Frontend (HTML Structure)
**File: `core/templates/core/dashboard.html`**
```html
<div class="stats-grid">
    <div class="stat-card">
        <h3>Total Disruptions</h3>
        <p id="totalDisruptions">0</p>
    </div>
    <!-- More cards... -->
</div>
<div class="charts-container">
    <canvas id="trendChart"></canvas>
</div>
```

## 6.3 Frontend (JavaScript Logic)
**File: `core/static/js/dashboard.js`**
```javascript
async function updateStats(disruptions) {
    const total = disruptions.length;
    const downtime = disruptions.reduce((sum, d) => sum + d.duration, 0);
    
    document.getElementById('totalDisruptions').textContent = total;
    document.getElementById('totalDowntime').textContent = `${downtime} min`;
    
    // Render Charts
    new Chart(ctx, {
        type: 'line',
        data: { ... }
    });
}
```

---

# 7. Conclusion
The **Domino Disruption Predictor** successfully addresses the problem of unmonitored productivity loss. By combining a user-friendly interface with data analytics, it empowers users to take control of their time. The project demonstrates the effective use of full-stack web technologies (Django + JavaScript) to solve real-world behavioral problems. Future enhancements, such as browser extensions and mobile apps, will further increase its utility and adoption.

---

# 8. Bibliography
1.  **Django Documentation:** https://docs.djangoproject.com/
2.  **Chart.js Documentation:** https://www.chartjs.org/
3.  **MDN Web Docs (HTML/CSS/JS):** https://developer.mozilla.org/
