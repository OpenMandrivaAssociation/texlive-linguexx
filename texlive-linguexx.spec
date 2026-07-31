%global tl_name linguexx
%global tl_revision 79758

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typesetting linguistic examples and glosses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/linguexx
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linguexx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linguexx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a standalone LaTeX package for linguistic examples, with a
`linguex`-compatible input syntax and first-class support for accessible
(tagged) PDF output. linguexx reimplements the familiar dot-syntax of
linguex on the expl3 engine, with no dependency on linguex, cgloss4e, or
xspace. It runs on pdfLaTeX, XeLaTeX and LuaLaTeX. When the document
enables the LaTeX tagging code, linguexx writes its examples into the
PDF structure tree as accessible objects.

