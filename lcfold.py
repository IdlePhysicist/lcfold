#
#	lcfold.py
#	Eoghan Conlon O'Neill, 2017
#
from numpy import round, array, vstack
def lcfold(data, period, transit_mid_point):
	"""
		data should be an array, in the case for which the function was written for data is a two column matrix from a fits file imported by astropy.
		It goes with out saying hopefully that
			` time = data[0] `
		But you know know.
		Parameters
		----------
			data => array, time = data[0]
			period
			transit_mid_point
			output defaulted to False, if True then a folded fits file is outputted.
	"""
	phase = (data[0] + transit_mid_point)/period
	phase = phase - round(phase)  # <- Copied from Ernst

	from astropy.io import fits
	'''
	if output == True:
		from astropy.io import fits
		array_0 = array(['Folded Lightcurve']) # There will only be one array
		col0 = fits.Column(name='Time', format='float64', array=a1)
		col1 = fits.Column(name='Flux', format='float64', array=a1)
		cols = fits.ColDefs([col0, col1])
		newFile = fits.BinTableHDU.from_columns(cols)
		#newFile = fits.PrimaryHDU(array_0)
		newFile.writeto('folded_LC.fits', clobber=True)
	'''

	hdu = fits.PrimaryHDU(vstack((phase, data[1])))   ##Save as 2d image
	hdu.writeto('folded_LC.fits', clobber=True)
	#print 'phase'
	return phase
