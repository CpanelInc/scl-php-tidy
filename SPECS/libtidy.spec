%define ns_prefix ea
%define pkg_base  libtidy
%define pkg_name  %{ns_prefix}-%{pkg_base}
%define _prefix   /opt/cpanel/%{pkg_base}
%define _unpackaged_files_terminate_build 0

Name:    %{pkg_name}
Summary: Utility to clean up and pretty print HTML/XHTML/XML
Version: 5.4.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4544 for more details
%define release_prefix 2
Release: %{release_prefix}%{?dist}.cpanel
Vendor: cPanel, Inc.

Group:   Applications/Text
License: W3C
URL:     http://tidy.sourceforge.net/

Source0: https://github.com/htacg/tidy-html5/releases/download/5.4.0/tidy-html5-5.4.0.tar.gz

BuildRequires: cmake

Provides: %{pkg_name} = %{version}-%{release}

%description
When editing HTML it's easy to make mistakes. Wouldn't it be nice if
there was a simple way to fix these mistakes automatically and tidy up
sloppy editing into nicely layed out markup? Well now there is! Dave
Raggett's HTML TIDY is a free utility for doing just that. It also
works great on the atrociously hard to read markup generated by
specialized HTML editors and conversion tools, and can help you
identify where you need to pay further attention on making your pages
more accessible to people with disabilities.

%package devel
Summary: Development files for %{name}
Group:   Development/Libraries
Provides: %{pkg_name}-devel = %{version}-%{release}
Requires: %{pkg_name} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -n tidy-html5-%{version}

%build

cd build/cmake
cmake ../.. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/cpanel/libtidy -DLIB_INSTALL_DIR=%{_lib}

%install

cd build/cmake
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_prefix}

%dir %{_prefix}/bin
%attr(0755,root,root) %{_prefix}/bin/tidy

%dir %{_prefix}/%{_lib}
%{_prefix}/%{_lib}/libtidy*

%files -n %{pkg_name}-devel
%defattr(-,root,root,-)

%dir %{_prefix}/include
%{_prefix}/include/*.h

%changelog
* Fri May 22 2020 Julian Brown <julian.brown@cpanel.net> - 5.4.0-2
- ZC-6850: Fix for C8

* Mon Sep 25 2017 Dan Muey <dan@cpanel.net> - 5.4.0-1
- EA-6819: Update libtidy from 0.99.0 to 5.4.0

* Mon Feb 06 2017 Dan Muey <dan@cpanel.net> - 0.99.0-35
- EA-5946: Change Provides to ea4 specific name so yum does not tie in non ea4 libtidy

* Wed Feb 01 2017 Dan Muey <dan@cpanel.net> - 0.99.0-34
- EA-5945: clean -devel paths that may or may not exist in post uninstall

* Wed Feb 01 2017 Dan Muey <dan@cpanel.net> - 0.99.0-33
- EA-5935: properly cleanup empty dirs when removed

* Tue Jan 31 2017 Cory McIntire <cory@cpanel.net> - 0.99.0-32
- EA-5419: repackage for use as an EA4 RPM

* Tue Dec 03 2013 Pavel Raiskup <praiskup@redhat.com> - 0.99.0-31.20091203
- silence gcc's warnings for -Werror=format-string (#1037356)

* Thu Oct 10 2013 Pavel Raiskup <praiskup@redhat.com> - 0.99.0-30.20091203
- enable testsuite during package build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-29.20091203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Pavel Raiskup <praiskup@redhat.com> - 0.99.0-28.20091203
- add manual page for tab2space

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-27.20091203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-26.20091203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Rex Dieter <rdieter@fedoraproject.org> 0.99.0-25.20091203
- rebuild 2, the wrath of doxygen (#831423)

* Thu Jun 14 2012 Rex Dieter <rdieter@fedoraproject.org> 0.99.0-24.20091203
- rebuild fyand (for yet another newer doxygen) (#831423)

* Wed Jun 13 2012 Rex Dieter <rdieter@fedoraproject.org> 0.99.0-23.20091203
- rebuild for newer doxygen, avoid html doc multilib conflict (#831423)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-22.20091203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-21.20091203
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.99.0-20.20091203
- 20091203 snapshot
- spec housecleaning
- Tidy erroniously removes whitespace, causing mangled text (#481350)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-19.20070615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-18.20070615
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Rex Dieter <rdieter@fedoraproject.org> 0.99.0-17.20070615
- respin (gcc43)

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.99.0-16.20070615
- respin (BuildID)

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.99.0-15.20070615
- License: W3C

* Tue Jul 31 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.99.0-14.20070615
- BR: libtool (again)

* Mon Jul 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.99.0-13.20070615
- 2007-06-15 snapshot

* Wed Feb 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.99.0-12.20070228
- 2007-02-28 snapshot

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-11.20051025
- fc6 respin

* Wed Jul 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-10.20051025
- fc6 respin

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Fri Jan 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-9.20051025
- libtidy returns to be multilib friendly

* Wed Oct 26 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-8.20051025
- Update to 051025 and docs to 051020

* Tue Aug  9 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-7.20050803
- -devel: Provides: libtidy-devel (#165452)

* Tue Aug  9 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-6.20050803
- cleanup doc generation
- add/restore missing docs (manpage, quickref.html)

* Mon Aug  8 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0.99.0-5.20050803
- Update to 050803 and docs to 050705
- simplify (fedora.us bug #2071)
- drop missing manpage

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.99.0-4.20041214
- rebuild on all arches

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Dec 16 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-2.20041214
- Update to 041214 and docs to 041206.
- Build with dependency tracking disabled.

* Sun Oct  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040916
- Update to 040916 and docs to 040810.

* Fri Aug 13 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040811
- Update to 040811, patches applied upstream.

* Wed Jul 28 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040720
- Update to 040720.
- Add partial fix (still incorrect for XHTML 1.1) for usemap handling.

* Mon Jul  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040704
- Update to 040704.

* Fri Jun 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040622
- Update to 040622.

* Sat Jun  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040603
- Update to 040603.

* Sat May 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040514
- Update to 040514.

* Sun May  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.2.20040318
- Update docs to 040317, and generate API docs ourselves.

* Fri Mar 19 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040318
- Update to 040318.

* Tue Mar 16 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040315
- Update to 040315.

* Mon Mar 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040314
- Update to 040314.

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040313
- Update to 040313.

* Sun Feb  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040205
- Update to 040205.

* Wed Feb  4 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040202
- Update to 040202.

* Sun Feb  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040130
- Update to 040130.

* Sun Jan 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040124
- Update to 040124.
- Honor optflags more closely.

* Sun Jan 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040110
- Update to 040110.

* Thu Jan  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040106
- Update to 040106.

* Tue Jan  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20040104
- Update to 040104.

* Sun Nov  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20031101
- Update to 031101.

* Thu Oct 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20031029
- Update to 031029.

* Fri Oct  3 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20031002
- Update to 031002.

* Sat Sep 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20030926
- Update to 030926.

* Wed Sep  3 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20030901
- Update to 030901.

* Sat Aug 16 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20030815
- Update to 030815.

* Sat Aug  2 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20030801
- Update to 030801.

* Mon Jul 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.99.0-0.fdr.1.20030716
- First build.
