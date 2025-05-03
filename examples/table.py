"""Example usage of the table formatting utility."""

import logging

from maa import format_table_log

logger = logging.getLogger(__name__)


def main() -> None:
    employee_data = [
        {"id": 101, "name": "Alice Wonderland", "dept": "Engineering", "salary": 95000.50},
        {"dept": "Marketing", "salary": 82000.00, "id": 102, "name": "Bob The Builder"},
        {"name": "Charlie Chaplin", "id": 103, "dept": "HR", "salary": 78550.75},
        {"id": 104, "name": "Diana Prince", "dept": "Engineering", "salary": 110000.0},
        {"id": 105, "name": "VeryLong NameIndeed Here", "dept": "Super Long Department Name", "salary": 65000.0},
    ]

    # Define the legend
    employee_legend = [
        {"data_key": "id", "header": "Emp ID", "width": 7},
        {"data_key": "name", "header": "Employee Name", "width": 20},
        {"data_key": "dept", "header": "Department", "width": 15},
        {"data_key": "salary", "header": "Salary", "width": 10},
    ]

    # Format the table
    table_string = format_table_log("Employee Details", employee_legend, employee_data)

    # Log the table
    logger.info("Formatted Employee Table:\n%s", table_string)

    perf_data = [
        {"metric": "Latency", "value": 123.4567, "target": 150.0},
        {"metric": "Error Rate", "value": 0.01234, "target": 0.05},
        {"metric": "Throughput", "value": 10500.8, "target": 10000.0},
    ]
    perf_legend = [
        {"data_key": "metric", "header": "Metric", "width": 12},
        {"data_key": "value", "header": "Value", "width": 8},  # Width might cause truncation/rounding
        {"data_key": "target", "header": "Target", "width": 8},
    ]

    perf_table = format_table_log("Performance Metrics", perf_legend, perf_data)
    logger.info("\n%s", perf_table)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    main()
