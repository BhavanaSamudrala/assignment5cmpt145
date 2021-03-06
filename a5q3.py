# Bhavana Samudrala
# student number- 11258695
# NSID- bhs053
# Instructor- Arlin Schaffel
# CMPT-145-L14

import node as N

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
        NOTE: THIS VERSION OF THE FUNCTION IS KNOWN TO BE BROKEN!!!
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        walker = walker.get_next()
        # print the data
        result = '[ {} |'.format(str(value))
        while walker is not None:
            value = walker.get_data()
            walker = walker.get_next()
            result += ' *-]-->[ {} |'.format(str(value))
            # represent the next with an arrow-like figure


        # at the end of the chain, use '/'
        result += ' / ]'

    return result
