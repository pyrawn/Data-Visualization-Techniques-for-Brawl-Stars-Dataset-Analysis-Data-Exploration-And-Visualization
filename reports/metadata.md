# Metadata for Cleaned Brawl Stars Datasets

## Dataset Source
- **Original Dataset by**: Alberto Vidal
- **Data Collection Source**: Brawl Stars API
- **Available on**: Kaggle
- **Original Format**: CSV
- **Purpose**: Rankings and statistics for players and clubs in Brawl Stars, a mobile game by Supercell.

---

## Description of Cleaned Datasets

Three datasets have been cleaned for analysis from the original data uploaded by Alberto Vidal. These datasets focus on rankings and other related attributes for top players and clubs, including general club rankings, rankings for players using the character Jessie, and rankings specifically for clubs in Mexico.

### 1. Jessie Players Ranking
- **Entries**: 200
- **Columns**: 9
- **Description**: This dataset contains information on the top 200 players who primarily use Jessie as their character. Attributes include player tags, names, icon IDs, trophies count, rank, and club information.
- **Cleaned Columns**:
  - `tag`: Unique identifier for each player.
  - `name`: Player's name.
  - `nameColor`: Color code for the player's name.
  - `icon`: Player's icon ID.
  - `trophies`: Total trophies earned by the player.
  - `rank`: Player's rank.
  - `club`: Associated club of the player.
  - `normalized_trophies` and `normalized_rank`: Normalized values for trophies and rank to enable comparative analysis.
- **Data Types**: Integer, Float, Object
- **Memory Usage**: 14.2 KB

### 2. Clubs Ranking
- **Entries**: 200
- **Columns**: 129
- **Description**: This dataset includes comprehensive information about the top 200 clubs globally. Each row represents a club and contains various attributes related to club structure, player membership, and ranking.
- **Cleaned Columns**:
  - `Rank`: Club ranking.
  - `tag`: Unique club ID.
  - `name`: Club name.
  - `description`: Club description.
  - `type`: Club type.
  - `requiredTrophies`: Trophies required to join the club.
  - `trophies`: Total trophies of the club.
  - `member_1_tag` - `member_30_tag`, `member_1_name` - `member_30_name`, `member_1_role` - `member_30_role`, `member_1_trophies` - `member_30_trophies`: Information on each of the top 30 members of the club, including ID, name, role in the club, and trophy count.
  - `trophies_normalized` and `requiredTrophies_normalized`: Normalized values for trophies and required trophies.
- **Data Types**: Integer, Float, Object
- **Memory Usage**: 201.7 KB

### 3. Mexico Clubs Ranking
- **Entries**: 199
- **Columns**: 8
- **Description**: This dataset lists the top-ranking clubs located in Mexico. Each entry includes details on rank, tag, name, badge, trophies, member count, and normalized values for trophies and member count.
- **Cleaned Columns**:
  - `Rank`: Club rank.
  - `tag`: Unique identifier for each club.
  - `name`: Club name.
  - `badgeId`: Badge identifier for the club.
  - `trophies`: Total trophies held by the club.
  - `memberCount`: Number of members in the club.
  - `trophies_normalized` and `member_count_normalized`: Normalized values to assist in comparative analysis.
- **Data Types**: Integer, Float, Object
- **Memory Usage**: 14.0 KB
