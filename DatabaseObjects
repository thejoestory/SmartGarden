CREATE TABLE [dbo].[smart_garden_temp](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[sensor] [varchar](50) NULL,
	[temp] [varchar](50) NULL,
	[humidity] [varchar](50) NULL,
	[captureDate] [datetime] NULL,
 CONSTRAINT [PK_smart_garden_temp] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

CREATE TABLE [dbo].[smart_garden_moisture](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[sensor] [varchar](50) NULL,
	[reading] [varchar](50) NULL,
	[capturedate] [datetime2](7) NULL,
 CONSTRAINT [PK_smart_garden_moisture] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

CREATE TABLE [dbo].[smart_garden_light](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[sensor] [varchar](50) NULL,
	[reading] [varchar](50) NULL,
	[capturedate] [datetime2](7) NULL,
 CONSTRAINT [PK_smart_garden_light] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


CREATE PROCEDURE [dbo].[smart_garden_LogLight]
@sensorID VARCHAR(50),
@reading VARCHAR(50)
AS

INSERT INTO smart_garden_light (sensor, reading, capturedate)
VALUES (@sensorID, @reading, GETDATE())

GO

CREATE PROCEDURE [dbo].[smart_garden_LogTemp]
@sensorid VARCHAR(50),
@temp VARCHAR(50),
@humidity VARCHAR(50)
AS

INSERT INTO smart_garden_temp (sensor, temp, humidity, capturedate)
VALUES (@sensorid, @temp, @humidity, GETDATE())

GO

CREATE PROCEDURE [dbo].[smart_garden_LogMoisture]
@sensorID VARCHAR(50),
@reading VARCHAR(50)
AS

INSERT INTO smart_garden_moisture (sensor, reading, capturedate)
VALUES (@sensorID, @reading, GETDATE())

GO
