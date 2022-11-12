class ListExercise:
    @staticmethod
    def get_max(input_list: list[int]) -> int:
        max_item = input_list[0]

        for item in input_list:
            if item > max_item:
                max_item = item

        return max_item

    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if not input_list:
            return input_list

        max_item = ListExercise.get_max(input_list)

        processed_list = list(map(lambda num: max_item if num > 0 else num, input_list))

        return processed_list

    @staticmethod
    def get_search_result(input_list: list[int], query: int, low: int, high: int) -> int:
        if not input_list or low > high:
            return -1

        mid = (low + high) // 2

        if input_list[mid] > query:
            return ListExercise.get_search_result(input_list, query, low, mid - 1)
        elif input_list[mid] < query:
            return ListExercise.get_search_result(input_list, query, mid + 1, high)
        else:
            return mid

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        return ListExercise.get_search_result(input_list, query, 0, len(input_list) - 1)
