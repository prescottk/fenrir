install it.
1. build it
make -f /usr/share/selinux/strict/include/Makefile fenrir.pp
2. install it
semodule -i /path/to/fenrir.pp


# created with that
# systemctl start fenrir
# ausearch -c '(r-daemon)' --raw | audit2allow -M fenrir
# semodule -X 300 -i fenrir.pp

