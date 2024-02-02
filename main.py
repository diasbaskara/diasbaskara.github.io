def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def referensi():
        f = open("templates/referensi.md", "r")
        return f.read()