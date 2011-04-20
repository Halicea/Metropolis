#{%block imports%}
from Controllers import MetropolisControllers
#{%endblock%}

webapphandlers = [
#{%block ApplicationControllers %}
#{%block MetropolisControllers%}
('/(.*)', MetropolisControllers.ObjectTypes),
('/(.*)/(.*)', MetropolisControllers.ObjectTypes),
('/(.*)/(.*)/(.*)', MetropolisControllers.ObjectTypes),
#{%endblock%}
#{%endblock%}
]

