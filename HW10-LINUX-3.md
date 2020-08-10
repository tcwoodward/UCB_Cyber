### Tar
#### Stripping Components
- **Exercise 1**
  - Extract `Movies`: `tar xvf TarDocs.tar --strip=1 TarDocs/Movies`
  - Extract `Movies/ZOE_0004.mp4`: `tar xvf TarDocs.tar --strip=2 TarDocs/Movies/ZOE_0004.mp4`

#### Modifying Archives
- **Exercise 1**

```bash
  # Insert the solution commands for Exercise 1 below
cp sample.tar update.tar
touch text{1..2}.txt
tar rvf update.tar text{1..2}.txt
```

- **Exercise 2**

```bash
  # Insert the solution commands for Exercise 2 below
tar uvf update.tar text2.txt
```

- **Exercise 3**
```bash
  # Insert the solution commands for Exercise 3 below
tar f update.tar --delete text1.txt
```

#### Incremental Backups
- **Exercise 1**
  - A **snapshot file** is `An incremental archive with additional metadata stored in a standalone file`.
  - A **backup level** is `a type of backup. There are different backup ‘levels’ for the type of backup taking place.
`.
  - A **level 0 backup** is `A full backup`.

- **Exercise 2**

```bash
  # Insert the solution commands for Exercise 2 below
sudo tar --create --listed-incremental=/var/log/home.snar --file=/var/backups/home_backup.0.tar /home
touch ~/new_file.1 ~/new_file.2
cp /var/log/home.snar /var/log/home.snar-1
sudo tar --create --listed-incremental=/var/log/home.snar-1 --file=/var/backups/home_backup.1.tar /home
```

### Cron
#### Managing cron
Please paste the contents of `backup-cron-jobs.txt` in the space below.

```bash
  # Paste the contents of `backup-cron-jobs.txt` below
  */2 * * * 2,4,6 tar cf ~/data/cron/Documents/cronjob.tar $(find ~/Projects/TarDocs/Documents/ -iname '*.txt') && tar xf ~/data/cron/Documents/cronjob.tar -C ~/data/cron/exercises >/dev/null 2>&1

```
