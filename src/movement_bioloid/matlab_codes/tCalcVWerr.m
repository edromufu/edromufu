function err = tCalcVWerr(Cref, Cnow)

perr = Cref.p - Cnow.p;
Rerr = Cnow.R' * Cref.R;
werr = Cnow.R * trot2omega(Rerr);

err = [perr; werr];