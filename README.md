# TaskFlow-Planner
### Project Overview
TaskFlow Planner is a web-based task management application designed to help users track and organize tasks by priority and deadline. It offers a simple and user-friendly interface that allows users to add tasks, assign priority levels, and set deadlines. Tasks are displayed with a progress bar to track completion, and a dynamic countdown shows how many days are left until each task's deadline.
The application is built using Flask, a lightweight Python web framework, along with front-end technologies such as HTML, CSS, and JavaScript.

### Project Objectives
- **To develop a functional to-do list application where users can manage their tasks efficiently.**
- **To implement task sorting based on priority and deadlines.**
- **To provide users with visual feedback on task completion through progress bars.**
- **To offer a dynamic countdown for deadlines, creating urgency and helping with prioritization.**


### Techniques and Methodology
**Flask (Back-End)**
The back-end of the project is developed using Flask, a lightweight web framework that allows easy setup and management of web applications. Flask is used to handle routing, form submissions, and interaction with the front-end.
Routing: Flask handles the HTTP routes of the application:
- **"/": Displays the welcome page with a simple login form.**
- **"/task_page": Displays the form to add new tasks with fields for task name, priority, and deadline.**
- **"/task_list": Displays the list of tasks, with each task showing the priority, deadline, progress, and a checkbox to mark it as completed.**


**Front-End**
The front-end is developed using HTML for structure, CSS for styling, and JavaScript for dynamic interactions.

- **HTML:**
Forms for user input (task name, priority, deadline).
Task lists for displaying tasks.
- **CSS:**
Ensures a clean and simple layout for easy navigation.
Style elements such as buttons, forms, and progress bars.
- **JavaScript:**
Dynamic updating of the progress bar based on completed tasks.
Countdown to each task's deadline, updating in real-time.

**Task Management and Sorting**
- **Task Prioritization: Each task is assigned a priority (High, Medium, Low), which is then used to sort tasks in order of importance.**
- **Deadline Tracking: Each task has a deadline that is processed and displayed with a countdown timer (e.g., "3 days left").**


**Dynamic Features**
- **Task Progress Bar:**
A visual bar is displayed to show the completion status of tasks. This helps users see at a glance how many tasks are completed.
The progress bar is updated dynamically using JavaScript.
- **Countdown for Deadlines:**
JavaScript is used to calculate the remaining time before a task's deadline and display the result in real-time. The countdown dynamically updates to show users how much time remains to complete each task.


### Libraries and Tools Used
**Flask**
- **Flask: The main Python web framework used to develop the application, handling routing and rendering templates. Flask also processes user inputs from forms and handles page navigation.
Version: Flask 2.x**




### Instructions for Running the Project

- **Step 1: Clone the Repository:**
git clone https://github.com/yourusername/your-repository.git

- **Step 2: Create a Virtual Environment**

- **Step 3: Activate the Virtual Environment**

- **Step 4: Install Dependencies**

- **Step 5: Run the Application**

- **Step 6: Using the App**
- **Welcome Page: Enter any username and password and press "Next."**
- **Task Page: Enter a task, select a priority level (High, Medium, Low), and set a deadline. Add multiple tasks if needed.**
- **Task List Page: View all the tasks you’ve added with a progress bar for completed tasks and a countdown showing how many days are left until the deadline for each task.**


#### Finally 
The TaskFlow Planner successfully achieves the goal of providing a simple yet effective task management tool. It allows users to add tasks, track their progress, and prioritize their work based on deadlines and importance. The use of Flask for the back-end and HTML/CSS/JavaScript for the front-end ensures that the app is lightweight, responsive, and easy to extend in the future.
