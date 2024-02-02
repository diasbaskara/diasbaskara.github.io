def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def referensi():
        f = open("templates/referensi.md", "r")
        lines = [
            '*[DPP]: Dasar Pengenaan Pajak',
            '*[PTKP]: Penghasilan Tidak Kena Pajak',
            '*[NPWP]: Nomor Pokok Wajib Pajak',
            '*[PPh]: Pajak Penghasilan',
            '*[PPN]: Pajak Pertambahan Nilai',
            '*[OP]: Orang Pribadi',
        ]
        multiline_string = '\n'.join(lines)
        return f.read()