from radical.htbac import Esmacs, Runner


def main():

    ht = Runner()

    esmacs1 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk1',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs2 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk2',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs3 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk3',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs4 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk4',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs5 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk5',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs6 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk6',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs7 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk7',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])

    esmacs8 = Esmacs(number_of_replicas=25,
                     system='brd4-gsk8',
                     workflow=['eq0', 'eq1', 'eq2', 'sim1'])


    ht.add_protocol(esmacs1)
    ht.add_protocol(esmacs2)
    ht.add_protocol(esmacs3)
    ht.add_protocol(esmacs4)
    ht.add_protocol(esmacs5)
    ht.add_protocol(esmacs6)
    ht.add_protocol(esmacs7)
    ht.add_protocol(esmacs8)
    
    
    ht.cores = 64
    ht.rabbitmq_config(hostname='localhost', port=32821)
    ht.run()


if __name__ == '__main__':
    import os

    os.environ['RADICAL_ENTK_VERBOSE'] = 'INFO'
    os.environ['RADICAL_PILOT_DBURL'] = 'mongodb://htbac-user:password@ds131826.mlab.com:31826/htbac-isc-experiments'
    os.environ['RP_ENABLE_OLD_DEFINES'] = 'True'
    os.environ['SAGA_PTY_SSH_TIMEOUT'] = '2000'
    os.environ['RADICAL_PILOT_PROFILE'] = 'True'
    os.environ['RADICAL_ENMD_PROFILE'] = 'True'
    os.environ['RADICAL_ENMD_PROFILING'] = '1'

    main()