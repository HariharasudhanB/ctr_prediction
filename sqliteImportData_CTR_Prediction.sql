drop table if exists trainData;

CREATE TABLE trainData(click INT, weekday INT, hour INT, time_stamp DATE, logType INT, user_id TEXT, userAgent TEXT, IP TEXT, region TEXT, city TEXT, adExchange TEXT, domain TEXT, URL TEXT, anonymousURL_id TEXT, adSlot_id TEXT, adSlotWidth INT, adSlotHeight INT, adSlotVisibility INT, adSlotFormat INT, adSlotFloorPrice INT, creative_id TEXT, keyPageURL TEXT, advertiser_id TEXT, userTags TEXT);

.separator "	"
.import train.txt trainData

drop table if exists testData;

CREATE TABLE testData(weekday INT, hour INT, time_stamp DATE, logType INT, user_id TEXT, userAgent TEXT, IP TEXT, region TEXT, city TEXT, adExchange TEXT, domain TEXT, URL TEXT, anonymousURL_id TEXT, adSlot_id TEXT, adSlotWidth INT, adSlotHeight INT, adSlotVisibility INT, adSlotFormat INT, adSlotFloorPrice INT, creative_id TEXT, keyPageURL TEXT, advertiser_id TEXT, userTags TEXT);

.separator "	"
.import test.txt testData