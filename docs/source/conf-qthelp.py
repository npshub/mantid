# -*- coding: utf-8 -*-# Mantid Repository : https://github.com/mantidproject/mantid
#
# Copyright &copy; 2018 ISIS Rutherford Appleton Laboratory UKRI,
#   NScD Oak Ridge National Laboratory, European Spallation Source,
#   Institut Laue - Langevin & CSNS, Institute of High Energy Physics, CAS
# SPDX - License - Identifier: GPL - 3.0 +

# All configuration values have a default; values that are commented out
# serve to show the default.
#
# Options here are applied and assumed to be those required when the builder is set the "html".
# For common options see conf.py.in. This file is presumed to be "execfiled" by the main conf.py.in

# -- Override options for non-embedded standalone HTML output --------------------------------------

# Theme-specific options to customize the look and feel of a theme.
# We config the bootstrap settings here, and apply CSS changes in
# custom.css rather than here.

# html_theme used to be used for both html and qthelp. From Sphinx 1.5.0 onwards the qthelp builder
# for Python 3 uses qthelp_theme and qthelp_theme_options instead of the html_theme and html_theme_options.
# Leave both in here in case old Sphinx version is ever used
html_theme_options = {
    # Navigation bar title.
    'navbar_title': " ", # deliberate single space so it's not visible
    # Tab name for entire site.
    'navbar_site_name': "Mantid",
    # Add links to the nav bar. Third param of tuple is true to create absolute url.
    'navbar_links': [
    ],
    # Do not show the "Show source" button.
    'source_link_position': "no",
    # Remove the local TOC from the nav bar
    'navbar_pagenav': False,
    # Hide the next/previous in the nav bar.
    'navbar_sidebarrel': False,
    # Use the latest version.
    'bootstrap_version': "3",
    # Ensure the nav bar always stays on top of page.
    'navbar_fixed_top': "false",
}

qthelp_theme_options = {
    # Navigation bar title.
    'navbar_title': " ", # deliberate single space so it's not visible
    # Tab name for entire site.
    'navbar_site_name': "Mantid",
    # Add links to the nav bar. Third param of tuple is true to create absolute url.
    'navbar_links': [
    ],
    # Do not show the "Show source" button.
    'source_link_position': "no",
    # Remove the local TOC from the nav bar
    'navbar_pagenav': False,
    # Hide the next/previous in the nav bar.
    'navbar_sidebarrel': True,
    # Use the latest version.
    'bootstrap_version': "3",
    # Ensure the nav bar always stays on top of page.
    'navbar_fixed_top': "false",
}

plot_html_show_formats = False
plot_html_show_source_link = False
