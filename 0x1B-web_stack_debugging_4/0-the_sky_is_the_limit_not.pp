# fix cuncurrent users number
exec {'cuncurrent':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf && sed -i '$a ULIMIT=\"-n 15\"' /etc/default/nginx && sudo service nginx restart"
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
