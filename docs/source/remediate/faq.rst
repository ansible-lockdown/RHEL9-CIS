FAQ
===

Does this role work only with |benchmark_os_short|?
-----------------------------------------------------

No -- it works on multiple distributions!

The |benchmark_name| guidance is designed to ONLY be applicable to |benchmark os|
systems and if you are using this role in a regulated organization you should be aware 
that applying these settings to distributions other than listed is unsupported
and may run afoul of your organization or regulatory bodies guidelines during a compliance
audit. It is on YOU to understand your organizations requirements and the laws and regulations
you must adhere to before applying this role.

See :ref:`system_applicability_ref_label` below for more details on applying this role to non-RedHat EL 7
or CentOS 7 systems.

Why should this role be applied to a system?
--------------------------------------------

There are three main reasons to apply this role to production Linux systems:

Improve security posture
  The configurations from the |benchmark_name| add security and rigor around multiple
  components of a Linux system, including user authentication, service
  configurations, and package management. All of these configurations add up
  to an environment that is more difficult for an attacker to penetrate and use
  for lateral movement.

Meet compliance requirements
  Some deployers may be subject to industry compliance programs, such as
  PCI-DSS, ISO 27001/27002, or NIST 800-53. Many of these programs require
  hardening standards to be applied to systems.

Deployment without disruption
  Security is often at odds with usability. The role provides the greatest
  security benefit without disrupting production systems. Deployers have the
  option to opt out or opt in for most configurations depending on how their
  environments are configured.

.. _system_applicability_ref_label:

Which systems are covered?
--------------------------------------------------------

This role and the |benchmark_name| guidance it implements are fully applicable to servers
(physical or virtual) and containers running the following Linux distributions:

* |benchmark_os|



The role is tested against each distribution to ensure that tasks run properly.
it is idempotent, and  an Audit is used to run a compliance scan after the role
is applied to test compliance with the STIG standard.

Which systems are not covered?
------------------------------

This role will run properly against a container (docker or other), however
this is not recommended and is only really useful during the development and
testing of this role (ie most CI systems provide containers and not full VMs),
so this role must be able to run on and test against containers.

Again for those in the back...applying this role against a container
in order to secure it is generally a *BAD* idea. You should be applying this
role to your container hosts and then using other hardening guidance that is
specific to the container technology you are using (docker, lxc, lxd, etc)
