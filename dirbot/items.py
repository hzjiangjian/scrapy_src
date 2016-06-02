from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    url = Field()

    def self_print(self):
        print "####################### start ##########################"

        print "name:"
        print self["name"]

        print "description:"
        print self["description"]

        print "url"
        print self["url"]

        print "####################### end ##########################"



