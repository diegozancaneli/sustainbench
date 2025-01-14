import argparse

import sustainbench


def main() -> None:
    """
    Downloads the latest versions of all specified datasets,
    if they do not already exist.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--root_dir', required=True,
        help='The directory where [dataset]/data can be found (or should be '
             'downloaded to, if it does not exist).')
    parser.add_argument(
        '--datasets', nargs='*', default=None,
        help='A space-separated list of dataset names to download. If left '
             'unspecified, the script will download all of the official '
             'benchmark datasets. Available choices are '
             f'{sustainbench.supported_datasets}.')
    config = parser.parse_args()

    if config.datasets is None:
        config.datasets = sustainbench.benchmark_datasets

    for dataset in config.datasets:
        if dataset not in sustainbench.supported_datasets:
            raise ValueError('{dataset} not recognized; must be one of '
                             f'{sustainbench.supported_datasets}.')

    print(f'Downloading the following datasets: {config.datasets}')
    for dataset in config.datasets:
        print(f'=== {dataset} ===')
        sustainbench.get_dataset(
            dataset=dataset,
            root_dir=config.root_dir,
            download=True)


if __name__ == '__main__':
    main()
