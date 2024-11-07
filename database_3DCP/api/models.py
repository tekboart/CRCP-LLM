from django.db import models

# Create your models here.

#TODO: (ME) I think I should have a class for each node type
#TODO: (ME) Then use attributes (specific for each node type)
class Node(models.Model):
    """
    #TODO: Finish class docstring
    """
    node_type = models.CharField(max_length=100)
    parent_node_id = models.IntegerField()
    # TODO: how to have a list of node features (that are specific to each node_type)
    # node_features = models.Li

    def __str__(self):
        return self.node_type
        # return "???"

# TODO: create an "Edge" class too
class Edge(models.Model):
    pass
