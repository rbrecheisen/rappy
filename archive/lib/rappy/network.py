class Node(object):

    def __init__(self):
        self.inputs = {}
        self.inputs_desc = {}
        self.inputs_types = {}
        self.outputs = {}
        self.outputs_desc = {}
        self.outputs_types = {}
        self.params = {}
        self.params_defaults = {}
        self.params_desc = {}
        self.params_types = {}

    def get_info(self):
        info = ''
        info += '##########################################################\n'
        info += '# {}\n'.format(self.__class__.__name__)
        info += '##########################################################\n'
        info += '# Inputs:\n'
        if len(self.inputs.keys()) == 0:
            info += '- None\n'
        for k in self.inputs.keys():
            info += '# - {} ({})\n'.format(k, self.inputs_types[k])
        info += '# \n'
        info += '# Outputs:\n'
        if len(self.outputs.keys()) == 0:
            info += '# - None\n'
        for k in self.outputs.keys():
            info += '# - {} ({})\n'.format(k, self.outputs_types[k])
        info += '# \n'
        info += '# Parameters:\n'
        if len(self.params.keys()) == 0:
            info += '# - None\n'
        for k in self.params.keys():
            info += '# - {} ({}) (default: {})\n'.format(k, self.params_types[k], self.params_defaults[k])
        info += '##########################################################\n'
        return info

    # Input

    def add_input(self, name, data_type, desc=None):
        self.inputs[name] = None
        self.inputs_types[name] = data_type
        self.inputs_desc[name] = desc

    def get_input(self, name):
        return self.inputs[name]

    def get_input_desc(self, name):
        return self.inputs_desc[name]

    def get_input_type(self, name):
        return self.inputs_types[name]

    def set_input(self, name, value):
        self.inputs[name] = value

    def get_inputs(self):
        return self.inputs

    # Output

    def add_output(self, name, data_type, desc=None):
        self.outputs[name] = None
        self.outputs_types[name] = data_type
        self.outputs_desc[name] = desc

    def get_output(self, name):
        self.execute()
        return self.outputs[name]

    def get_output_desc(self, name):
        return self.outputs_desc[name]

    def get_output_type(self, name):
        return self.outputs_types[name]

    def set_output(self, name, value):
        self.outputs[name] = value

    def get_outputs(self):
        return self.outputs

    # Parameters

    def add_param(self, name, data_type, default=None, desc=None):
        self.params[name] = default
        self.params_types[name] = data_type
        self.params_defaults[name] = default
        self.params_desc[name] = desc

    def get_param(self, name):
        return self.params[name]

    def get_param_default(self, name):
        return self.params_defaults[name]

    def get_param_desc(self, name):
        return self.params_desc[name]

    def get_param_type(self, name):
        return self.params_types[name]

    def set_param(self, name, value):
        self.params[name] = value

    def get_params(self):
        return self.params

    # Execute

    def execute(self):
        raise NotImplementedError('execute() is not implemented')
