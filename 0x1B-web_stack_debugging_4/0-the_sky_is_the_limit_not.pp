# fix cuncurrent users number
exec {'cuncurrent':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart'
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/etc/init.d/', '/usr/local/bin/:/bin']
}
