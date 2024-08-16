class AlgorithmException(Exception):
    pass

    def get_message(self):
        raise NotImplementedError


class MinVikubilNotMetException(AlgorithmException):

    def get_message(self):
        return "Minimum Vikubil is not met"


class MaximumAllocationsExceededException(AlgorithmException):

    def get_message(self):
        return "Maximum Allocations have been exceeded"



