from git import Repo, NoSuchPathError, GitCommandError, GitError


def clone_repository(url, path):
    try:
        Repo.clone_from(url, path)
    except NoSuchPathError:
        print('{} not exist!'.format(path))
    except GitCommandError as e:
        print(e)
    except GitError as e:
        print(e)



