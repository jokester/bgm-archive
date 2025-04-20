import click
import tqdm
from pathlib import Path
from collections import Counter
from ..loader.wiki_archive_loader import WikiArchiveLoader


@click.command("validate-archive")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def validate_wiki_archive(path: Path):
    """
    Validate a Bangumi wiki archive by iterating through all entity types.

    Args:
        path: Path to the archive file

    Returns:
        Counter with counts of each entity type
    """
    loader = WikiArchiveLoader(
        str(path), silent_validation_error=True, stop_on_error=False
    )
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
