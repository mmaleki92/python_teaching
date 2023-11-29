## Singleton Pattern Problem:

- Problem: Create a logging system for an application. Ensure that the logging class is a singleton, so that all parts of the application use the same logger instance.
Task: Implement a Logger class as a singleton. This class should have a method log(message) to write messages to a log file. Ensure that every instance of this class is the same.

## Factory Method Pattern Problem:

- Problem: Design a simple application for creating different types of charts (e.g., bar chart, pie chart, line chart).
Task: Implement a ChartFactory that has a method create_chart(type) which returns different chart objects based on the input type. Define classes like BarChart, PieChart, and LineChart that have a common method draw().
## Observer Pattern Problem:

- Problem: Create a weather monitoring system where a weather station collects data and multiple display elements (like current conditions, weather statistics, and forecasts) update in real-time as the data changes.
Task: Implement a WeatherStation class (subject) and various display classes (observers). When the weather station changes its readings (temperature, humidity, etc.), all registered displays should automatically update their information.

## Strategy Pattern Problem:

- Problem: Develop a sorting application that can use different sorting algorithms depending on the nature of the data.
Task: Define a SortStrategy interface with an execute method. Implement different sorting algorithms (like bubble sort, quick sort, merge sort) as strategies. The context class should be able to switch sorting strategies based on user input or data type.

## Decorator Pattern Problem:

- Problem: Build a pizza ordering system where you can dynamically add toppings to a pizza and calculate the total cost accordingly.
Task: Implement a Pizza interface with a method get_cost(). Create a BasePizza class and different decorator classes for toppings like Cheese, Peppers, Ham, etc. Each topping decorator should modify the get_cost method to add its own cost to the base price.