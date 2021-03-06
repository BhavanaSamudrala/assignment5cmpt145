# Bhavana Samudrala
# student number- 11258695
# NSID- bhs053
# Instructor- Arlin Schaffel
# CMPT-145-L14

import node as N

def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data values, calculate
        the sum of the data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing
                           numeric data values
    Post-condition:
            None
    Return
            :return: the sum of the data values in the node chain
    """

    if node_chain is None:
        return 0
    return (node_chain.get_data()+sumnc(node_chain.get_next()))



def count_in(node_chain, value):
    """
    Purpose:
        Counts the number of times a value appears in a node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param value: a data value
    Return:
        :return: The number times the value appears in the node chain
    """

    count = 0
    while (node_chain is not None):
        if node_chain.get_data() == value:
            count += 1
        node_chain = node_chain.get_next()
    return count



def replace_in(node_chain, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Post-conditions:
        Each occurrence of the target value in the chain is replaced with
        the replacement value.
    Return:
        None
    """
    while (node_chain is not None):
        if node_chain.get_data() == target:
            node_chain.set_data(replacement)
        node_chain = node_chain.get_next()
