#!/usr/bin/env python

if __name__ == "__main__":

    from optparse import OptionParser

    usage = "Usage: %prog -d <datafile or metafile> -m <modelfile> [options]"
    parser = OptionParser(usage)
    #parser.add_option("-h", "--help",
    #                  action="store_true", dest="help", default=False,
    #                  help="Show this help message and exit.")
    parser.add_option("-d", "--datafiles",
                      action="store", metavar="archive", dest="datafiles",
                      help="PSRCHIVE archive from which to measure TOAs/DMs, or a metafile listing archive filenames.")
    parser.add_option("-m", "--modelfile",
                      action="store", metavar="model", dest="modelfile",
                      help="Model file from ppgauss.py, ppspline.py, or PSRCHIVE FITS file that either has same channel frequencies, nchan, & nbin as datafile(s), or is a single profile (nchan = 1, with the same nbin) to be interpreted as a constant template.")
    parser.add_option("-e", "--ext",
                      action="store", metavar="extension", dest="ext",
                      default=".resids",
                      help="Extention to filename, in addition to .png.")
    parser.add_option("-n", "--nowb",
                      action="store_false", dest="wb",
                      default=True,
                      help="Don't use pptoas.py, rather fit each channel's phase and amplitude individually of the others.  Will use header DM to dedisperse.")
    parser.add_option("-r", "--rot",
                      default=0.0,
                      action="store", metavar="phase", dest="rot_phase",
                      help="Additional rotation to add to plots. [default=0.0]")
    parser.add_option("--showplot",
                      action="store_true", dest="show_plot", default=False,
                      help="Show a plot of fitted data/model/residuals for each subint.  Good for diagnostic purposes only.")
    parser.add_option("--quiet",
                      action="store_true", dest="quiet", default=False,
                      help="Less text to stdout.")

    (options, args) = parser.parse_args()

    if (options.datafiles is None or options.modelfile is None):
        print "\nmake_residual_plots.py - make residual plots of model and data profiles\n"
        parser.print_help()
        print ""
        parser.exit()

    datafiles = options.datafiles
    modelfile = options.modelfile
    ext = options.ext
    wb = options.wb
    rot_phase = float(options.rot_phase)
    show_plot = options.show_plot
    quiet = options.quiet

    if wb:
        from pptoas import *
        gt = GetTOAs(datafiles=datafiles, modelfile=modelfile, quiet=quiet)
        gt.get_TOAs(datafile=None, tscrunch=False, nu_refs=None, DM0=None,
            bary=True, fit_DM=True, fit_GM=False, fit_scat=False,
            log10_tau=True, scat_guess=None, fix_alpha=False,
            print_phase=False, print_flux=False, print_parangle=False,
            addtnl_toa_flags={}, method='trust-ncg', bounds=None, nu_fits=None,
            show_plot=False, quiet=quiet)
        for iarch, ok_idatafile in enumerate(gt.ok_idatafiles):
            datafile = gt.datafiles[ok_idatafile]
            for isub in gt.ok_isubs[iarch]:
                if show_plot:
                    gt.show_fit(datafile=datafile, isub=isub, rotate=rot_phase,
                        show=True, return_fit=False, quiet=True)
                gt.show_fit(datafile=datafile, isub=isub, rotate=rot_phase,
                        show=True, return_fit=False,
                        savefig=datafile+".sub%d"%isub+ext+".png", quiet=True)
    else:
        from pplib import *
        if file_is_type(datafiles, "ASCII"):
            datafiles = [datafile[:-1] for datafile in \
                    open(datafiles, "r").readlines()]
        else:
            datafiles = [datafiles]
        all_ok_idatafiles = []
        all_ok_isubs = []
        for iarch, datafile in enumerate(datafiles):
            #Load data
            try:
                data = load_data(datafile, dedisperse=True,
                        dededisperse=False, tscrunch=False,
                        pscrunch=True, fscrunch=False, rm_baseline=True,
                        flux_prof=False, refresh_arch=False, return_arch=False,
                        quiet=quiet)
                if not len(data.ok_isubs):
                    if not quiet:
                        print "No subints to fit for %s.  Skipping it."%\
                                datafile
                    continue
                else: all_ok_idatafiles.append(iarch)
            except RuntimeError:
                if not quiet:
                    print "Cannot load_data(%s).  Skipping it."%datafile
                continue
            #Unpack the data dictionary into the local namespace; see load_data
            #for dictionary keys.
            for key in data.keys():
                exec(key + " = data['" + key + "']")
            all_ok_isubs.append(ok_isubs)
            for isub in ok_isubs:
                port = subints[isub,0] * masks[isub,0]
                model_name, model = read_spline_model(modelfile, freqs[isub],
                        nbin, quiet=True)
                model = model * masks[isub,0]
                if rot_phase: model = rotate_data(model, rot_phase)
                for ichan in ok_ichans[isub]:
                    dprof = port[ichan]
                    mprof = model[ichan]
                    err = noise_stds[isub,0,ichan]
                    r = fit_phase_shift(dprof, mprof, err)
                    port[ichan] = rotate_profile(dprof, r.phase)
                    model[ichan] *= r.scale
            #for iarch, ok_idatafile in enumerate(all_ok_idatafiles):
            #    datafile = datafiles[ok_idatafile]
            #    for isub in all_ok_isubs[iarch]:
                titles = ("%s\nSubintegration %d"%(datafile, isub),
                        "Fitted Model %s"%(model_name), "Residuals")
                if show_plot:
                    show_residual_plot(port=port, model=model, resids=None,
                            phases=phases, freqs=freqs[isub],
                            noise_stds=noise_stds[isub,0], nfit=2,
                            titles=titles, rvrsd=bool(bw < 0))
                show_residual_plot(port=port, model=model, resids=None,
                        phases=phases, freqs=freqs[isub],
                        noise_stds=noise_stds[isub,0], nfit=2,
                        titles=titles, rvrsd=bool(bw < 0),
                        savefig=datafile+".sub%d"%isub+ext+".png")
