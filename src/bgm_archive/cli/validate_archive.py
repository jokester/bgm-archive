import click
import tqdm
from pathlib import Path
from collections import Counter
from ..loader.wiki_archive_loader import WikiArchiveLoader


def validate_wiki_archive(path: Path):
    """
    Validate a Bangumi wiki archive by iterating through all entity types.

    Args:
        path: Path to the archive file

    Returns:
        Counter with counts of each entity type
    """
    loader = WikiArchiveLoader(str(path))
    entity_counts = Counter()

    # Process subjects
    print("Validating subjects...")
    for _ in tqdm.tqdm(loader.subjects(), desc="Subjects"):
        entity_counts["subjects"] += 1

    # Process persons
    print("Validating persons...")
    for _ in tqdm.tqdm(loader.persons(), desc="Persons"):
        entity_counts["persons"] += 1

    # Process characters
    print("Validating characters...")
    for _ in tqdm.tqdm(loader.characters(), desc="Characters"):
        entity_counts["characters"] += 1

    # Process episodes
    print("Validating episodes...")
    for _ in tqdm.tqdm(loader.episodes(), desc="Episodes"):
        entity_counts["episodes"] += 1

    # Process subject relations
    print("Validating subject relations...")
    for _ in tqdm.tqdm(loader.subject_relations(), desc="Subject Relations"):
        entity_counts["subject_relations"] += 1

    # Process subject persons
    print("Validating subject-person relations...")
    for _ in tqdm.tqdm(loader.subject_persons(), desc="Subject-Person Relations"):
        entity_counts["subject_persons"] += 1

    # Process subject characters
    print("Validating subject-character relations...")
    for _ in tqdm.tqdm(loader.subject_characters(), desc="Subject-Character Relations"):
        entity_counts["subject_characters"] += 1

    # Process person characters
    print("Validating person-character relations...")
    for _ in tqdm.tqdm(loader.person_characters(), desc="Person-Character Relations"):
        entity_counts["person_characters"] += 1

    # Print summary
    print("\nValidation Summary:")
    for entity_type, count in entity_counts.items():
        print(f"  {entity_type}: {count}")

    return entity_counts


@click.command()
@click.argument("archive_path", type=click.Path(exists=True, path_type=Path))
def validate_archive(archive_path: Path):
    """
    Validate a Bangumi wiki archive file.

    This command iterates through all entity types in the archive,
    validates them against their respective models, and provides
    a summary of the entities found.

    ARCHIVE_PATH: Path to the Bangumi wiki archive file (.zip)
    """
    print(f"Validating archive: {archive_path}")
    entity_counts = validate_wiki_archive(archive_path)

    total_entities = sum(entity_counts.values())
    print(f"\nTotal entities validated: {total_entities}")

    if total_entities > 0:
        print("Archive validation completed successfully!")
    else:
        print("Warning: No entities found in the archive.")
        return 1

    return 0


if __name__ == "__main__":
    validate_archive()
