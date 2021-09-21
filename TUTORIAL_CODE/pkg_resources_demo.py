# get package version

import pkg_resources
print(pkg_resources.get_distribution("fire").version)
# 0.1.3
