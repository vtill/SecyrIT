all: ../out/index.html ../out/show_ssid.html ../out/test.html ../out/status.html ../out/update.html ../out/wifi_2.html

../out/index.html:index.m4
	m4 index.m4 > ../out/index.html
../out/show_ssid.html:show_ssid.m4
	m4 $< > $@
../out/test.html:test.m4
	m4 $< > $@
../out/status.html:status.m4
	m4 $< > $@
../out/update.html:update.m4
	m4 $< > $@
../out/wifi_2.html:wifi_2.m4
	m4 $< > $@

copy:
	cp ../out/* ../../
clean:
	rm ../out/*

