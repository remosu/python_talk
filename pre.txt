.. -*- mode: rst -*-

.. include:: <s5defs.txt>

========================
python en el laboratorio
========================

------------------------------------------------------------------------------------
¿`python`:orange: `vs`:huge: `awk + bash + gnuplot + matlab + Fortran/C/C++`:green:?
------------------------------------------------------------------------------------

.. image:: images/logo.png
    :align: center


\
==

.. class:: center

    `awk bash perl gnuplot matlab matemathica Fortran C/C++`:green:

    `¿por qué python?`:huge:


\
==

.. image:: images/googleit.png
    :align: center


python es fácil de aprender
===========================

* sintaxis clara
* compacto
* pocas reglas
* ... y pocas excepciones



pseudo código
==============

.. class:: handout

    El código se lee mas de lo que se escribe

.. sourcecode:: pseudocode

    E = 0
    para cada partícula i en la simulación
        E = E + V_i^2

C
===================

.. sourcecode:: c

    int energy = 0;
    int i;
    for(i=0; i<n; i++)
    {
        double vx = velocities[i][0];
        double vy = velocities[i][1];
        double vz = velocities[i][2];
        energy += vx*vx + vy*vy + vz*vz;
    }

python
========================

.. sourcecode:: python

    energy = 0
    for i in range(n):
        vx = velocities[i].v[0]
        vy = velocities[i].v[1]
        vz = velocities[i].v[2]
        energy += vx**2 + vy**2 + vz**2

python
======================

.. sourcecode:: python

    energy = 0
    for velocity in velocities:
        vx = velocity[0]
        vy = velocity[1]
        vz = velocity[2]
        energy += vx**2 + vy**2 + vz**2

python
======================

.. sourcecode:: python

    energy = 0
    for velocity in velocities:
        vx, vy, vz = velocity[i]
        energy += vx**2 + vy**2 + vz**2

python
======================

.. sourcecode:: python

    energy = 0
    for vx, vy, vz in velocities:
        energy += vx**2 + vy**2 + vz**2


ágil
====

.. class:: center

    `editar >> compilar >> ejecutar >> editar`:green:

    `VS`:huge:

    `editar >> ejecutar >> editar`:orange:



baterias incluidas
==================


baterias incluidas 2.0
======================

baterias incluidas 2.0
======================

ipython
-------

.. image:: images/ipython.png
    :align: center


baterias incluidas 2.0
======================

scypy/numpy
-----------

baterias incluidas 2.0
======================

matplotlib
----------


acelerando python
=================


SWIG - bost.python
==================


weave - instant
===============


f2py
====


cython
======


