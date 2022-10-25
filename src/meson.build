pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'monitorets')
gnome = import('gnome')

gnome.compile_resources('monitorets',
  'monitorets.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'monitorets.in',
  output: 'monitorets',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

monitorets_sources = [
  '__init__.py',
  'main.py',
  'event_broker.py',
  'events.py',
  'monitor_type.py',
  'preferences.py',
  'controller.py',
  'theming.py',
]

install_data(monitorets_sources, install_dir: moduledir)

install_subdir('ui', install_dir: moduledir)
install_subdir('samplers', install_dir: moduledir)
