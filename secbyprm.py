import numpy as np

class secbyprm:

    def search(self, enervals, datarray, minener, maxener, minth, maxth, mu_hist):
        prm_prv = np.copy(datarray[0,7:12])
        identity = np.zeros(len(enervals), float)
        mucount = np.zeros(len(enervals), float)
        hist_ener = np.zeros(len(enervals), float)
        check_id = True
        countmu = 0

        for line in datarray:
            if line[10] > minth and line[10] < maxth:
                identity = np.copy(line[7:12])
                check_id = np.allclose(prm_prv, identity)
            if check_id:
                countmu += 1

            else:
                if prm_prv[2] > minener*enervals[0] and prm_prv[2] < maxener*enervals[0]:
                    mu_hist[0].append(countmu)

                elif prm_prv[2] > minener*enervals[1] and prm_prv[2] < maxener*enervals[1]:
                    mu_hist[1].append(countmu)

                elif prm_prv[2] > minener*enervals[2] and prm_prv[2] < maxener*enervals[2]:
                    mu_hist[2].append(countmu)

                elif prm_prv[2] > minener*enervals[3] and prm_prv[2] < maxener*enervals[3]:
                    mu_hist[3].append(countmu)
                
                elif prm_prv[2] > minener*enervals[4] and prm_prv[2] < maxener*enervals[4]:
                    mu_hist[4].append(countmu)

                elif prm_prv[2] > minener*enervals[5] and prm_prv[2] < maxener*enervals[5]:
                    mu_hist[5].append(countmu)

                countmu = 1
                prm_prv = identity.copy()

        for i in range(len(mu_hist)):
            tmp = np.array(mu_hist[i])
            if len(tmp) > 0:
                hist_ener[i] = tmp.mean() / 3600.

        return hist_ener
