# Collaborators: Fill in names and SUNetIDs here

def query_one():
    """Query for Columbia's venue"""
    return """
SELECT
  DISTINCT venue_name,
  venue_capacity
FROM
  `bigquery-public-data.ncaa_basketball.mbb_games_sr`
WHERE
  season = 2013
  AND h_market = 'Columbia'
  AND venue_state = 'NY'
    """

def query_two():
    """Query for games in Columbia's venue"""
    return """
SELECT
  COUNT(DISTINCT(game_id)) num
FROM
  `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr`
WHERE
  season = 2013
  AND venue_name = "Francis S. Levien Gymnasium" 
  """

def query_three():
    """Query for highest attendance"""
    return """      
SELECT
  h_market,
  attendance,
  season
FROM
  `bigquery-public-data.ncaa_basketball.mbb_games_sr`
ORDER BY
  attendance DESC
LIMIT
  3
   """

def query_four():
    """Query for Columbia's wins at home"""
    return """
SELECT
  COUNT(*) number,
  ROUND(AVG(points_game),2) avg_columbia,
  ROUND(AVG(opp_points_game),2) avg_opponent
FROM
  `bigquery-public-data.ncaa_basketball.mbb_historical_teams_games`
WHERE
  market = 'Columbia University-Barnard College'
  AND win=TRUE
  AND season BETWEEN 2009
  AND 2016    
  
  """

def query_five():
    """Query for players for birth state"""
    return """
SELECT
  COUNT(DISTINCT player_id) AS num_players
FROM
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` player
INNER JOIN
  `bigquery-public-data.ncaa_basketball.mbb_teams` team
ON
  player.team_market = team.market
  AND player. birthplace_state = team.venue_state    
  """

def query_six():
    """Query for biggest total points"""
    return """
SELECT
  win_name,
  lose_name,
  win_pts,
  lose_pts,
  (win_pts + lose_pts) AS total_points
FROM
  `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`
ORDER BY
  total_points DESC
LIMIT
  1    
  """

def query_seven():
    """Query for historical upset percentage"""
    return """
SELECT
  ROUND(100*(COUNT(days_from_epoch) / (
      SELECT
        COUNT(days_from_epoch)
      FROM
        `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`)),2) AS upset_percentage
FROM
  `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`
WHERE
  lose_seed < win_seed and win_pts > 60  
 """

def query_eight():
    """Query for teams with same states and first letter"""
    return """
SELECT
  A.name AS teamA,
  B.name AS teamB,
  A.venue_state AS state
FROM
  `bigquery-public-data.ncaa_basketball.mbb_teams` A,
  `bigquery-public-data.ncaa_basketball.mbb_teams` B
WHERE
  A.name < B.name
  AND SUBSTR(A.name, 0, 1) = SUBSTR(B.name, 0, 1)
  AND A.venue_state = B.venue_state
ORDER BY
  teamA
LIMIT
  3
    """

def query_nine():
    """Query for top geographical locations"""
    return """
SELECT
  player.birthplace_city,
  player.birthplace_state,
  player.birthplace_country,
  SUM(player.points) AS total_points
FROM
  `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` player
WHERE
  player.team_market ='Columbia'
  AND season BETWEEN 2013
  AND 2016
GROUP BY
  player.birthplace_city,
  player.birthplace_state,
  player.birthplace_country
ORDER BY
  SUM(player.points) DESC
LIMIT
  3    
  """

def query_ten():
    """Query for teams with lots of high-scorers"""
    return """
SELECT
  team_market,
  COUNT(DISTINCT id) AS num_players
FROM (
  SELECT
    team_market,
    player_id AS id,
    SUM(points_scored)
  FROM
    `bigquery-public-data.ncaa_basketball.mbb_pbp_sr`
  WHERE
    (period = 2)
  GROUP BY
    game_id,
    team_market,
    player_id
  HAVING
    SUM(points_scored) >= 15) C
GROUP BY
  team_market
HAVING
  COUNT(DISTINCT id) > 5
ORDER BY
  COUNT(DISTINCT id) DESC,
  team_market
LIMIT
  5    
  """

def query_eleven():
    """Query for bottom performer teams"""
    return """
SELECT
  market,
  COUNT(season) as bottom_performer_count
FROM (
  SELECT
    A.season AS season,
    B.market AS market,
    A.losses
  FROM (
    SELECT
      season,
      MAX(losses)AS losses
    FROM
      `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons`
    GROUP BY
      season
    HAVING
      season BETWEEN 1900
      AND 2000 ) A,
    `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons` B
  WHERE
    A.season = B.season
    AND A.losses = B.losses
  ORDER BY
    A.season) C
GROUP BY
  market
HAVING
  market IS NOT NULL
ORDER BY
  COUNT(season) DESC,
  market
LIMIT
5
    """
    
    
