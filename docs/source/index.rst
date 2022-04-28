=========================================================
Automated security hardening for Linux hosts with Ansible
=========================================================

What is security hardening?
---------------------------

The content delivered is based upon either one of the two major contributors to the security best practices in the IT industry.

- Center for Internet Security (CIS): https://www.cisecurity.org/cis-benchmarks/
  - A global IT community of experts helping to build, document sets of benchmarks to produce industry best security practices

or

- Security Technical Implementation Guide (STIG): https://public.cyber.mil/stigs/downloads/
  - From the Defense Information Systems Agency (DISA) 
  - The STIG is released with a public domain license and it is commonly used to secure systems at public and private organizations around the world.

Both are well known and respected benchmarks created for the industry to assist in achieving recognised compliance (e.g. PCI DSS, HIPAA, SOC2, NIST) and adopting security best practices.


What is provided?
-----------------

The content provided is open source licensed configurations to assist in achieving or auditing compliance to one of the benchmark providers listed above.

This consists of two components

- Audit
- Remediate

Both can be run alone or inconjunction with each other.

What do the roles do?
----------------------

- Audit 
  - runs a small single binary on the system written in go called goss: http://goss.rocks
  - enables you to very quickly scan your host and output the status of compliance for your host.

- Remediate
  - Ability to run from a central location using the configuration management tool ansible
  - Assists in bringing your host into compliance for the relevant benchmark


How do we do this?
------------------

We analyze each configuration control from the applicable benchmark to determine what impact it has on a live production environment and how to
best implement a way to audit the current configuration and how to achieve those requirements using Ansible. 
Tasks are added to the role that configure a host to meet the configuration requirements. Each task is documented to explain what was changed, why it was changed, and what deployers need to understand about the change.

Deployers have the option to enable/disable every control that does not suit their environments needs. 
Every control item has an associated variable that can be used to switch it on or off.

Additionally, the items that have configurable values, i.e. number of password attempts, will generally have a corresponding variable that allows for customization of the applied value.
It is imperative for each deployer to understand the regulations and compliance requirements that their organization and specific environments are responsible for meeting in order to effeectively implement the controls in the relevant benchmark.


Documentation
-------------

Documentation is split in the two categories

.. toctree::
   :maxdepth: 2
   audit
   remediate

Content list
------------
.. code-block: txt
  .. include:: benchmarks.rst
