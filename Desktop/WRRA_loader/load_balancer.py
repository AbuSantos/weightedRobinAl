# This algorithm distributes tasks to workers based on their weights.
# Its suitable for task allocation to workers efficiently, considering their different processing capacities.
# It calculates the Greatest Common Divisor (GCD) of weights to determine step size for task allocation,


class RoundRobinBalancer:
    """
    Initialize the RoundRobinBalancer with a list of tasks.

    Parameters:
    - tasks (list): A list of tasks, where each task is a dictionary with a "weight" attribute.
    """

    def __init__(self, tasks):
        self.tasks = tasks
        self.current_index = 0
        self.current_weight = self.gcd_weights()
        self.max_weight = max(tasks, key=lambda x: x["weight"])["weight"]

    def gcd(self, a, b):
        """
        Calculate the greatest common divisor of two numbers.

        Parameters:
        - a (int): The first number.
        - b (int): The second number.

        Returns:
        int: The greatest common divisor of a and b.
        """
        while b:
            a, b = b, a % b
        return a

    def advance_index(self):
        "Advance to the next index, updating weights if needed."
        self.current_index = (self.current_index + 1) % len(self.tasks)

    def gcd_weights(self):
        """
        Calculate the greatest common divisor of task weights.

        Returns:
        int: The greatest common divisor of task weights.
        """
        gcd = self.tasks[0]["weight"]
        for task in self.tasks[1:]:
            gcd = self.gcd(gcd, task["weight"])
        return gcd

    def get_next_task(self):
        """
        Get the next task based on Round Robin and weights.

        Returns:
        dict: The next task selected by the load balancer.
        """
        if not self.tasks:
            raise ValueError(
                "No tasks available. Please provide a non-empty list of tasks."
            )

        while True:
            self.current_index = (self.current_index + 1) % len(self.tasks)
            if self.current_index == 0:
                self.current_weight -= self.gcd_weights()
                if self.current_weight <= 0:
                    self.current_weight = self.max_weight
            if self.tasks[self.current_index]["weight"] >= self.current_weight:
                return self.tasks[self.current_index]
