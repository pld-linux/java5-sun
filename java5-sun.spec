# TODO:
# - package? /usr/lib/jvm/java-sun-1.5.0.12/jre/lib/deploy/ffjcext.zip
#
%define		_ver	1.5.0.22
%define		_src_ver	5.0u22
%define		_dir_ver	%(echo %{_ver}|sed 's/\\.\\(..\\)$/_\\1/')
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 49.0
Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Sun JDK - środowisko programistyczne Javy dla Linuksa
Name:		java5-sun
Version:	%{_ver}
Release:	4
License:	restricted, distributable
Group:		Development/Languages/Java
Source0:	http://download.java.net/dlj/binaries/jdk-%{_src_ver}-dlj-linux-i586.bin
# Source0-md5:	f3afc43863c8f529a81fe42bef912d8c
Source1:	http://download.java.net/dlj/binaries/jdk-%{_src_ver}-dlj-linux-amd64.bin
# Source1-md5:	d70398b2d6c1bd764330b7a3276c1e41
Source2:	Test.java
Patch0:		%{name}-ControlPanel-fix.patch
Patch1:		%{name}-desktop.patch
URL:		https://jdk-distros.dev.java.net/developer.html
BuildRequires:	file
BuildRequires:	rpm-build >= 4.3-0.20040107.21
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	unzip
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre = %{version}-%{release}
Provides:	j2sdk = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java-sun
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javareldir	%{name}-%{version}
%define		javadir		%{_jvmdir}/%{javareldir}
%define		jrereldir	%{javareldir}/jre
%define		jredir		%{_jvmdir}/%{jrereldir}
%define		jvmjardir	%{_jvmjardir}/%{name}-%{version}

# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libjava_crw_demo_g\.so.*' 'libmawt.so' 'java(ClassDataVersion)'
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

%description
This package symlinks Java SUN development tools provided by
java5-sun-jdk-base to system-wide directories like /usr/bin, making
Java SUN default JDK.

%description -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi programistycznych
uruchomieniowego Java SUN, dostarczanych przez pakiet
java5-sun-jdk-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Java SUN staje się domyślnym JDK w
systemie.

%package appletviewer
Summary:	Java applet viewer from Sun Java
Summary(pl.UTF-8):	Przeglądarka appletów Javy Suna
Group:		Development/Languages/Java
Requires:	%{name}-jdk-base = %{version}-%{release}

%description appletviewer
This package applet viewer for Sun Java.

%description appletviewer -l pl.UTF-8
Ten pakiet zawiera przeglądarkę appletów dla Javy Suna.

%package jdk-base
Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Sun JDK - środowisko programistyczne Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	jpackage-utils >= 0:1.6.6-14
Provides:	jdk(%{name})

%description jdk-base
Java Development Kit for Linux.

%description jdk-base -l pl.UTF-8
Środowisko programistyczne Javy dla Linuksa.

%package jre-jdbc
Summary:	JDBC files for Sun Java
Summary(pl.UTF-8):	Pliki JDBC dla Javy Suna
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	%{name}-jdbc
Obsoletes:	java-sun-jdbc

%description jre-jdbc
This package contains JDBC files for Sun Java.

%description jre-jdbc -l pl.UTF-8
Ten pakiet zawiera pliki JDBC dla Javy Suna.

%package jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
Requires:	jpackage-utils
Suggests:	%{name}-jre-X11
Provides:	java
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java(jaas) = %{version}
Provides:	java(jaf) = 1.1.1
Provides:	java(jaxp) = 1.3
Provides:	java(jaxp_parser_impl)
Provides:	java(jce) = %{version}
Provides:	java(jdbc-stdext) = %{version}
Provides:	java(jdbc-stdext) = 3.0
Provides:	java(jmx) = 1.4
Provides:	java(jndi) = %{version}
Provides:	java(jsse) = %{version}
Provides:	java1.4
Obsoletes:	java-blackdown-jre
Obsoletes:	jre
Obsoletes:	java(jaas)
Obsoletes:	java(jaf)
Obsoletes:	java(jaxp)
Obsoletes:	java(jaxp_parser_impl)
Obsoletes:	java(jce)
Obsoletes:	java(jdbc-stdext)
Obsoletes:	java(jdbc-stdext)
Obsoletes:	java(jmx)
Obsoletes:	java(jndi)
Obsoletes:	java(jsse)

%description jre
This package symlinks Java SUN runtime environment tools provided by
java5-sun-jre-base to system-wide directories like /usr/bin, making
Java SUN default JRE.

%description jre -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi środowiska
uruchomieniowego Java SUN, dostarczanych przez pakiet
java5-sun-jre-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Java SUN staje się domyślnym JRE w
systemie.

%package jre-base
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	jpackage-utils >= 0:1.6.6-14
Provides:	jre(%{name})

%description jre-base
Java Runtime Environment for Linux. Does not contain any X11-related
compontents.

%description jre-base -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa. Nie zawiera żadnych
elementów związanych ze środowiskiem X11.

%package jre-X11
Summary:	Sun JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Provides:	jre-X11 = %{version}
%ifarch %{ix86}
Provides:	javaws = %{version}
%endif

%description jre-X11
This package symlinks Java SUN X11 libraries provided by
java5-sun-jre-base-X11 to system-wide directories like /usr/bin,
making Java SUN default JRE-X11.

%description jre-X11 -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi X11 Java SUN,
dostarczanych przez pakiet java5-sun-jre-base-X11, w standardowych
systemowych ścieżkach takich jak /usr/bin, sprawiając tym samym, że
Java SUN staje się domyślnym JRE-X11 w systemie.

%package jre-base-X11
Summary:	Sun JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-base-X11
X11-related part of Java Runtime Environment for Linux.

%description jre-base-X11 -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa, część związana ze
środowiskiem graficznym X11.

%package jre-alsa
Summary:	JRE module for ALSA sound support
Summary(pl.UTF-8):	Moduł JRE do obsługi dźwięku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	%{name}-alsa
Obsoletes:	java-sun-alsa

%description jre-alsa
JRE module for ALSA sound support.

%description jre-alsa -l pl.UTF-8
Moduł JRE do obsługi dźwięku poprzez ALSA.

%package tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	jar
Provides:	java-jre-tools
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-jre-tools

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	jre

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.

%package -n browser-plugin-%{name}
Summary:	Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczki Javy do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java-sun-mozilla-plugin
Provides:	mozilla-firefox-plugin-java-sun
Provides:	mozilla-plugin-java-sun
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	java-sun-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java-sun
Obsoletes:	mozilla-firefox-plugin-gcc3-java-sun
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-firefox-plugin-java-sun
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java-sun
Obsoletes:	mozilla-plugin-gcc3-java-sun
Obsoletes:	mozilla-plugin-gcc32-java-sun
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun

%description -n browser-plugin-%{name}
Java plugin for WWW browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczki z obsługą Javy dla przeglądarek WWW.

%package sources
Summary:	JRE standard library sources
Summary(pl.UTF-8):	Źródła standardowej biblioteki JRE
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}

%description sources
Sources for the standard Java library.

%description sources -l pl.UTF-8
Źródła standardowej bilioteki Java.

%prep
%setup -q -T -c -n jdk%{_dir_ver}
cd ..
%ifarch %{ix86}
%{__unzip} -q %{SOURCE0} || :
%endif
%ifarch %{x8664}
%{__unzip} -q %{SOURCE1} || :
%endif
cd -
%ifnarch %{x8664}
%patch -P0 -p1
# patch only copy of the desktop file, leave original unchanged
cp jre/plugin/desktop/sun_java.desktop .
%patch -P1 -p1
%endif

# unpack packed jar files -- in %%prep as it is done "in place"
for pack in $(find . -name '*.pack'); do
	bin/unpack200 -r $pack ${pack%.pack}.jar
done

cp %{SOURCE2} Test.java

%build
./bin/javac Test.java
classver=$(file Test.class | grep -o 'compiled Java class data, version [0-9.]*' | awk '{print $NF}')
if [ "$classver" != %{_classdataversion} ]; then
	echo "Set %%define _classdataversion to $classver and rerun."
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jredir},%{javadir},%{jvmjardir},%{_javadir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_mandir}/{,ja/}man1,%{_prefix}/src/%{name}-sources} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_browserpluginsdir}}

cp -rf bin sample demo include lib $RPM_BUILD_ROOT%{javadir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

if test -f jre/lib/*/client/Xusage.txt ; then
mv -f jre/lib/*/client/Xusage.txt jre/Xusage.client
fi
if test -f jre/lib/*/server/Xusage.txt ; then
mv -f jre/lib/*/server/Xusage.txt jre/Xusage.server
fi
if test -f jre/lib/*.txt ; then
mv -f jre/lib/*.txt jre
fi
#mv jre/lib/font.properties{,.orig}
#mv jre/lib/font.properties{.Redhat6.1,}

cp -rf jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

# conflict with heimdal
for i in kinit klist ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/j$i
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/man1/j${i}.1
	mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/j${i}.1
done

for i in ControlPanel java java_vm keytool ktab orbd policytool \
	rmid rmiregistry servertool tnameserv ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in HtmlConverter appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap jconsole jdb jinfo jmap jps \
	 jsadebugd jstack jstat jstatd native2ascii rmic serialver ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

# make sure all tools are available under $(JDK_HOME)/bin
for i in ControlPanel keytool kinit klist ktab orbd policytool rmid \
		rmiregistry servertool tnameserv ; do
	ln -sf ../jre/bin/$i $RPM_BUILD_ROOT%{javadir}/bin/$i
done

rm -f $RPM_BUILD_ROOT%{javadir}/bin/{java,javaws}
ln -sf %{jredir}/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java
ln -sf %{jredir}/bin/javaws $RPM_BUILD_ROOT%{javadir}/bin/javaws

%ifarch %{ix86}
# copy _all_ plugin files (even those incompatible with PLD) --
# license restriction
cp -R jre/plugin $RPM_BUILD_ROOT%{jredir}

# Install plugin for browsers
# Plugin in regular location simply does not work (is seen by browsers):
ln -sf %{jredir}/plugin/i386/ns7/libjavaplugin_oji.so $RPM_BUILD_ROOT%{_browserpluginsdir}

install *.desktop $RPM_BUILD_ROOT%{_desktopdir}
install jre/plugin/desktop/*.png $RPM_BUILD_ROOT%{_pixmapsdir}
%endif

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{jvmjardir}/jce.jar
for f in jndi jndi-dns jndi-ldap jndi-cos jndi-rmi jaas jdbc-stdext jdbc-stdext-3.0 \
	sasl jaxp_parser_impl jaxp_transform_impl jaxp jmx xml-commons-apis; do
	ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{jvmjardir}/$f.jar
done

%ifnarch %{x8664}
install -d $RPM_BUILD_ROOT%{jredir}/javaws
cp -a jre/javaws/* $RPM_BUILD_ROOT%{jredir}/javaws
ln -sf %{jredir}/lib/javaws.jar $RPM_BUILD_ROOT%{jvmjardir}/javaws.jar

# leave all locale files unchanged in the original location (license
# restrictions) and only link them at the proper locations
for loc in `ls $RPM_BUILD_ROOT%{jredir}/lib/locale` ; do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
	ln -sf %{jredir}/lib/locale/$loc/LC_MESSAGES/sunw_java_plugin.mo \
		$RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
done

# standardize dir names
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh,zh_CN}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_HK.BIG5HK,zh_HK}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ko.UTF-8,zh.GBK,zh_TW.BIG5}
%endif

cp -a src.zip $RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources

ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java
ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/%{name}
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/jre
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/%{name}-jre
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/java
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jre

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans jre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT LICENSE README.html THIRDPARTYLICENSEREADME.txt
%{_jvmdir}/java
%{_jvmjardir}/java
%attr(755,root,root) %{_bindir}/HtmlConverter
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jsadebugd
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/serialver
%{_mandir}/man1/apt.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/jinfo.1*
%{_mandir}/man1/jmap.1*
%{_mandir}/man1/jps.1*
%{_mandir}/man1/jsadebugd.1*
%{_mandir}/man1/jstack.1*
%{_mandir}/man1/jstat.1*
%{_mandir}/man1/jstatd.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
%{_mandir}/man1/jconsole.1*
%lang(ja) %{_mandir}/ja/man1/apt.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/jinfo.1*
%lang(ja) %{_mandir}/ja/man1/jmap.1*
%lang(ja) %{_mandir}/ja/man1/jps.1*
%lang(ja) %{_mandir}/ja/man1/jsadebugd.1*
%lang(ja) %{_mandir}/ja/man1/jstack.1*
%lang(ja) %{_mandir}/ja/man1/jstat.1*
%lang(ja) %{_mandir}/ja/man1/jstatd.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/jconsole.1*

%files jdk-base
%defattr(644,root,root,755)
%{_jvmdir}/%{name}
%ifarch %{ix86}
%attr(755,root,root) %{javadir}/bin/HtmlConverter
%attr(755,root,root) %{javadir}/bin/ControlPanel
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%attr(755,root,root) %{javadir}/bin/javaws
%endif
%attr(755,root,root) %{javadir}/bin/apt
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/jinfo
%attr(755,root,root) %{javadir}/bin/jmap
%attr(755,root,root) %{javadir}/bin/jps
%attr(755,root,root) %{javadir}/bin/jsadebugd
%attr(755,root,root) %{javadir}/bin/jstack
%attr(755,root,root) %{javadir}/bin/jstat
%attr(755,root,root) %{javadir}/bin/jstatd
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/kinit
%attr(755,root,root) %{javadir}/bin/klist
%attr(755,root,root) %{javadir}/bin/ktab
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/orbd
%attr(755,root,root) %{javadir}/bin/policytool
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/servertool
%attr(755,root,root) %{javadir}/bin/tnameserv
%{javadir}/include
%dir %{javadir}/lib
%{javadir}/lib/*.jar
%{javadir}/lib/*.idl

%files appletviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{javadir}/bin/appletviewer
%{_mandir}/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*

%files jre-jdbc
%defattr(644,root,root,755)
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/lib/i386/libJdbcOdbc.so
%endif
%ifarch %{x8664}
%attr(755,root,root) %{jredir}/lib/amd64/libJdbcOdbc.so
%endif

%files jre-base
%defattr(644,root,root,755)
%{_jvmdir}/%{name}-jre
%attr(755,root,root) %{jredir}/bin/pack200
%attr(755,root,root) %{jredir}/bin/unpack200
%attr(755,root,root) %{javadir}/bin/pack200
%attr(755,root,root) %{javadir}/bin/unpack200
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%dir %{jredir}
%dir %{jredir}/bin
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/bin/java_vm
%endif
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/kinit
%attr(755,root,root) %{jredir}/bin/klist
%attr(755,root,root) %{jredir}/bin/ktab
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext
%ifarch %{ix86}
%dir %{jredir}/lib/i386
%dir %{jredir}/lib/i386/headless
%attr(755,root,root) %{jredir}/lib/i386/client
%attr(755,root,root) %{jredir}/lib/i386/native_threads
%attr(755,root,root) %{jredir}/lib/i386/server
%{jredir}/lib/i386/jvm.cfg
%attr(755,root,root) %{jredir}/lib/i386/lib[acdfhijmnrvz]*.so
%exclude %{jredir}/lib/i386/libjsoundalsa.so
%exclude %{jredir}/lib/i386/libjavaplugin*.so
%endif
%ifarch %{x8664}
%dir %{jredir}/lib/amd64
%dir %{jredir}/lib/amd64/headless
#%attr(755,root,root) %{jredir}/lib/i386/client
%attr(755,root,root) %{jredir}/lib/amd64/native_threads
%attr(755,root,root) %{jredir}/lib/amd64/server
%{jredir}/lib/amd64/jvm.cfg
%attr(755,root,root) %{jredir}/lib/amd64/lib[acdfhijmnrvz]*.so
%exclude %{jredir}/lib/amd64/libjsoundalsa.so
%endif
%{jredir}/lib/im
%{jredir}/lib/images
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%verify(not md5 mtime size) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
%lang(ja) %{jredir}/lib/*.properties.ja
%dir %{jvmjardir}
%{jvmjardir}/jaas.jar
%{jvmjardir}/jce.jar
%{jvmjardir}/jcert.jar
%{jvmjardir}/jdbc-stdext*.jar
%{jvmjardir}/jmx.jar
%{jvmjardir}/jndi*.jar
%{jvmjardir}/jnet.jar
%{jvmjardir}/jsse.jar
%{jvmjardir}/sasl.jar
%{jvmjardir}/jaxp*.jar
%{jvmjardir}/xml-commons*.jar
%{jredir}/lib/classlist
%{jredir}/lib/fontconfig.RedHat.2.1.bfc
%{jredir}/lib/fontconfig.RedHat.2.1.properties.src
%{jredir}/lib/fontconfig.RedHat.3.bfc
%{jredir}/lib/fontconfig.RedHat.3.properties.src
%{jredir}/lib/fontconfig.RedHat.8.0.bfc
%{jredir}/lib/fontconfig.RedHat.8.0.properties.src
%{jredir}/lib/fontconfig.RedHat.9.0.bfc
%{jredir}/lib/fontconfig.RedHat.9.0.properties.src
%{jredir}/lib/fontconfig.RedHat.bfc
%{jredir}/lib/fontconfig.RedHat.properties.src
%{jredir}/lib/fontconfig.SuSE.bfc
%{jredir}/lib/fontconfig.SuSE.properties.src
%{jredir}/lib/fontconfig.Sun.2003.bfc
%{jredir}/lib/fontconfig.Sun.2003.properties.src
%{jredir}/lib/fontconfig.Sun.bfc
%{jredir}/lib/fontconfig.Sun.properties.src
%{jredir}/lib/fontconfig.Turbo.8.0.bfc
%{jredir}/lib/fontconfig.Turbo.8.0.properties.src
%{jredir}/lib/fontconfig.Turbo.bfc
%{jredir}/lib/fontconfig.Turbo.properties.src
%{jredir}/lib/fontconfig.bfc
%{jredir}/lib/fontconfig.properties.src
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/lib/i386/gtkhelper
%attr(755,root,root) %{jredir}/lib/i386/headless/libmawt.so
%attr(755,root,root) %{jredir}/lib/i386/libsaproc.so
%attr(755,root,root) %{jredir}/lib/i386/libunpack.so
%endif
%ifarch %{x8664}
%attr(755,root,root) %{jredir}/lib/amd64/gtkhelper
%attr(755,root,root) %{jredir}/lib/amd64/headless/libmawt.so
%attr(755,root,root) %{jredir}/lib/amd64/libsaproc.so
%attr(755,root,root) %{jredir}/lib/amd64/libunpack.so
%endif
%dir %{jredir}/lib/management
%{jredir}/lib/management/jmxremote.access
%{jredir}/lib/management/jmxremote.password.template
%{jredir}/lib/management/management.properties
%{jredir}/lib/management/snmp.acl.template
%ifarch %{ix86}
%dir %{jredir}/lib/deploy
%{jredir}/lib/deploy/ffjcext.zip
%endif
%dir %{jredir}/lib/servicetag
%{jredir}/lib/servicetag/jdk_header.png


%files jre
%defattr(644,root,root,755)
%doc jre/{CHANGES,COPYRIGHT,LICENSE,README,*.txt}
%doc jre/Welcome.html
%doc jre/Xusage*
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/jkinit
%attr(755,root,root) %{_bindir}/jklist
%attr(755,root,root) %{_bindir}/ktab
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%{_jvmdir}/jre
%{_jvmjardir}/jre
%{_mandir}/man1/java.1*
%ifarch %{ix86}
%{_desktopdir}/sun_java.desktop
%{_pixmapsdir}/sun_java.png
%endif
%{_mandir}/man1/javaws.1*
%{_mandir}/man1/jkinit.1*
%{_mandir}/man1/jklist.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/ktab.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%{_mandir}/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/jkinit.1*
%lang(ja) %{_mandir}/ja/man1/jklist.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/ktab.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*

%files jre-base-X11
%defattr(644,root,root,755)
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/bin/javaws
%attr(755,root,root) %{jredir}/bin/ControlPanel
%endif
%attr(755,root,root) %{jredir}/bin/policytool
%{jredir}/lib/fonts
%{jredir}/lib/oblique-fonts
%ifarch %{ix86}
%dir %{jredir}/lib/i386/xawt
%dir %{jredir}/lib/i386/motif21
%attr(755,root,root) %{jredir}/lib/i386/awt_robot
%attr(755,root,root) %{jredir}/lib/i386/libjavaplugin*.so
%attr(755,root,root) %{jredir}/lib/i386/motif21/libmawt.so
%attr(755,root,root) %{jredir}/lib/i386/xawt/libmawt.so
%endif
%ifarch %{x8664}
%dir %{jredir}/lib/amd64
%dir %{jredir}/lib/amd64/xawt
%dir %{jredir}/lib/amd64/motif21
%attr(755,root,root) %{jredir}/lib/amd64/awt_robot
%endif
%ifarch %{ix86}
%{jvmjardir}/javaws.jar
%dir %{jredir}/lib/javaws
%{jredir}/lib/javaws/Java1.5.ico
%{jredir}/lib/javaws/messages.properties
%{jredir}/lib/javaws/messages_de.properties
%{jredir}/lib/javaws/messages_es.properties
%{jredir}/lib/javaws/messages_fr.properties
%{jredir}/lib/javaws/messages_it.properties
%{jredir}/lib/javaws/messages_ja.properties
%{jredir}/lib/javaws/messages_ko.properties
%{jredir}/lib/javaws/messages_sv.properties
%{jredir}/lib/javaws/messages_zh_CN.properties
%{jredir}/lib/javaws/messages_zh_HK.properties
%{jredir}/lib/javaws/messages_zh_TW.properties
%{jredir}/lib/javaws/miniSplash.jpg
%endif
%ifarch %{x8664}
%attr(755,root,root) %{jredir}/lib/amd64/motif21/libmawt.so
%attr(755,root,root) %{jredir}/lib/amd64/xawt/libmawt.so
%endif
%ifarch %{ix86}
%dir %{jredir}/javaws
%attr(755,root,root) %{jredir}/javaws/javaws
%endif

%files jre-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ControlPanel
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/bin/java_vm
%endif
%attr(755,root,root) %{_bindir}/policytool
%{_mandir}/man1/policytool.1*
%ifarch %{ix86}
%dir %{jredir}/lib/locale
%lang(de) %{jredir}/lib/locale/de
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%lang(es) %{jredir}/lib/locale/es
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%lang(fr) %{jredir}/lib/locale/fr
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%lang(it) %{jredir}/lib/locale/it
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%lang(ja) %{jredir}/lib/locale/ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko) %{jredir}/lib/locale/ko*
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%lang(sv) %{jredir}/lib/locale/sv
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_CN) %{jredir}/lib/locale/zh
%lang(zh_CN) %{jredir}/lib/locale/zh.*
%lang(zh_HK) %{jredir}/lib/locale/zh_HK*
%lang(zh_TW) %{jredir}/lib/locale/zh_TW*
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_HK) %{_datadir}/locale/zh_HK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo
%endif
%ifarch %{ix86}
%lang(ja) %{_mandir}/ja/man1/javaws.1*
%endif
%lang(ja) %{_mandir}/ja/man1/policytool.1*

%files jre-alsa
%defattr(644,root,root,755)
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/lib/i386/libjsoundalsa.so
%endif
%ifarch %{x8664}
%attr(755,root,root) %{jredir}/lib/amd64/libjsoundalsa.so
%endif

%files demos
%defattr(644,root,root,755)
%dir %{javadir}/demo
%{javadir}/demo/applets
%{javadir}/demo/jfc
%{javadir}/demo/jpda
%dir %{javadir}/demo/jvmti
%dir %{javadir}/demo/jvmti/[!i]*
%dir %{javadir}/demo/jvmti/*/lib
%attr(755,root,root) %{javadir}/demo/jvmti/*/lib/*.so
%{javadir}/demo/jvmti/*/src
%{javadir}/demo/jvmti/*/README*
%{javadir}/demo/jvmti/*/*.jar
%{javadir}/demo/jvmti/index.html
%{javadir}/demo/management
%ifarch %{ix86}
%{javadir}/demo/plugin
%{javadir}/demo/applets.html
%endif
%{javadir}/sample

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/rmic
%{_mandir}/man1/jar.1*
%{_mandir}/man1/rmic.1*
%{_mandir}/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*

%ifarch %{ix86}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%dir %{jredir}/plugin
%{jredir}/plugin/desktop
%dir %{jredir}/plugin/i386
%dir %{jredir}/plugin/i386/*
%attr(755,root,root) %{jredir}/plugin/i386/*/libjavaplugin_oji.so
%attr(755,root,root) %{_browserpluginsdir}/*.so
%endif

%files sources
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-sources
%{_prefix}/src/%{name}-sources/src.zip
