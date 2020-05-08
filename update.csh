#!/bin/csh

echo this is the update script

cd $MATTIME
echo searching for targets.dat in `pwd`
echo there are `wc -l targets.dat` pulsars to update

foreach pulsar (`cat targets.dat`) 
  echo working on pulsar $pulsar
  mkdir -p ${MATTIME}/${pulsar} 
  #go to where raw data resides
  cd $MEERTIME/timing/${pulsar}
  foreach obs (`ls -1 | grep 20`)
    cd $obs
    set beamno = `ls -1`
#    echo beamno is $beamno
    cd $beamno
    set freq = `ls -1` 
#    echo freq is $freq
    cd $freq
    set filecount = `ls -1 *.ar | wc -l`
    echo there are $filecount files in observation $obs for pulsar $pulsar
    echo -n creating soft links and directory...
    mkdir -p ${MATTIME}$pulsar/$obs/$beamno/$freq
    if (-f .linked) then
	echo already copied/linked $filecount archives for $obs
    else 
	foreach archive (`ls -1 *.ar`)
	    ln -s ${MEERTIME}$pulsar/$obs/$beamno/$freq/$archive ${MATTIME}$pulsar/$obs/$beamno/$freq/$archive
	end
	touch ${MATTIME}$pulsar/$obs/$beamno/$freq/.linked 
    endif
    cd ../../..
  end
  cd ..
end



 
