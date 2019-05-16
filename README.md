Ansible Kannel
=========

Install and configure [kannel](https://kannel.org).

Requirements
------------

The role has been developed and tested on Debian/Ubuntu 18.0.4

Role Variables
--------------
These are the role variables and default values
```yaml
kannel_install_extras: true # Install kannel extra packages for testing
kannel_enable_wap_box: false # Enable wapbox daemon
kannel_enable_sms_box: true # Enable smsbox daemon

```
#### Kannel configuration groups
Set the groups of configuration variables. Configuration for Kannel MUST always include a group for general bearerbox configuration. This group is named as 'core' in configuration file, and should be the first group in the configuration file.

```yaml
kannel_groups:
  - group: core # Required. Name of group
    admin-port: 13000 # The port number in which the bearerbox listens to HTTP administration commands.
    smsbox-port: 13001 # The port number to which the smsboxes, connect. use wapbox-port for WAP.
    admin-password: bar # Required. Password for HTTP administration commands 
    admin-deny-ip: "*.*.*.*" # The list of IPs to deny access to the HTTP administration. Default deny all.
    admin-allow-ip: "127.0.0.1" # The list of address to allow HTTP administration. Default allow local.
    log-file: "/var/log/kannel/bearerbox.log" # Location of general bearerbox logs
    access-log: "/var/log/kannel/bearerbox-access.log" # Location of bearerbox access logs
    box-deny-ip: "*.*.*.*" # These lists can be used to prevent box connections from given IP addresses. Default deny all.
    box-allow-ip: "127.0.0.1" # List of address to allow box connection from. Defailt allow local.

  - group: smsbox # You need an smsbox group to be able to use SMS Kannel. use wapbox for WAP.
    bearerbox-host: 127.0.0.1 # Address of the machine in which the bearerbox is running
    sendsms-port: 13013 # The port in which any sendsms HTTP requests are done. 
    log-file: /var/log/kannel/smsbox.log # Location of the general smsbox logs
    access-log: /var/log/kannel/smsbox-access.log # Location of access logs for the smsbox
    log-level: 0 # Log level verbosity. Values can be  0 to 5
    smsbox-id: mysmsbox # SMS box instance identifier used to identify an smsbox connected to a bearerbox for the purpose of having smsbox specific routing inside bearerbox.
  
  - group: smsbox-route # Performs smsbox routing inside bearerbox. Important if you have more than one SMSC
    smsbox-id: mysmsbox # Defines for which smsbox instance the routing rules do apply.
    smsc-id: "MY-SMSC" # If set, specifies from which smsc-ids all inbound messages should be routed to this smsbox instance
```
 
**Note on log level verbosity:**

`log-level` is a definition of minimum level of log-file events logged. 0 is for 'debug', 1 'info', 2 'warning, 3 'error' and 4 'panic' 

#### Extra kannel configuration files
To keep the main kannel configuration cleaner, you can seperate the config files and import them to the main kannel cofiguration. This would be a good place to keep `SMSC`, `sendsms-user` and  `sms-service` groups.

To include extra configurations files add each configuration file template and set the destination to copy it into the kannel server.
```yaml
kannel_include_config_files:
  - src: templates/etc/kannel/smpp.conf.j2 # Source of the config template file on the deployment host
    dest: /etc/kannel/smpp.conf # Absolute path to copy the config file to in the remote host.
```

Dependencies
------------

None.

Example Playbook
----------------



    - hosts: kannel
      roles:
         - role: kannel
           kannel_include_config_files:
             - src: smpp-configs.conf.j2
               dest: /etc/kannel/smpp-configs.conf
             
             - src: sendsms-configs.conf.j2
               dest: /etc/kannel/sendsms-configs.conf
               
             - src: 

License
-------

Apache V2

Author Information
------------------

[Ona](https://ona.io) Engineering.
