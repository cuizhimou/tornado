CREATE DATABASE `ihome` DEFAULT CHARACTER SET utf8;

use ihome;

CREATE TABLE ih_user_profile (
    up_user_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    up_name varchar(32) NOT NULL COMMENT '昵称',
    up_mobile char(11) NOT NULL COMMENT '手机号',
    up_passwd varchar(64) NOT NULL COMMENT '密码',
    up_real_name varchar(32) NULL COMMENT '真实姓名',
    up_id_card varchar(20) NULL COMMENT '身份证号',
    up_avatar varchar(128) NULL COMMENT '用户头像',
    up_admin tinyint NOT NULL DEFAULT '0' COMMENT '是否是管理员，0-不是，1-是',
    up_utime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    up_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (up_user_id),
    UNIQUE (up_name),
    UNIQUE (up_mobile)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8 COMMENT='用户信息表';

CREATE TABLE ih_area_info (
    ai_area_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '区域id',
    ai_name varchar(32) NOT NULL COMMENT '区域名称',
    ai_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (ai_area_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房源区域表';

CREATE TABLE ih_house_info (
    hi_house_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '房屋id',
    hi_user_id bigint unsigned NOT NULL COMMENT '用户ID',
    hi_title varchar(64) NOT NULL COMMENT '房屋名称',
    hi_price int unsigned NOT NULL DEFAULT '0' COMMENT '房屋价格，单位分',
    hi_area_id bigint unsigned NOT NULL COMMENT '房屋区域ID',
    hi_address varchar(512) NOT NULL DEFAULT '' COMMENT '地址',
    hi_room_count tinyint unsigned NOT NULL DEFAULT '1' COMMENT '房间数',
    hi_acreage int unsigned unsigned NOT NULL DEFAULT '0' COMMENT '房屋面积',
    hi_house_unit varchar(32) NOT NULL DEFAULT '' COMMENT '房屋户型',
    hi_capacity int unsigned NOT NULL DEFAULT '1' COMMENT '容纳人数',
    hi_beds varchar(64) NOT NULL DEFAULT '' COMMENT '床的配置',
    hi_deposit int unsigned NOT NULL DEFAULT '0' COMMENT '押金，单位分',
    hi_min_days int unsigned NOT NULL DEFAULT '1' COMMENT '最短入住时间',
    hi_max_days int unsigned NOT NULL DEFAULT '0' COMMENT '最长入住时间，0-不限制',
    hi_order_count int unsigned NOT NULL DEFAULT '0' COMMENT '下单数量',
    hi_verify_status tinyint NOT NULL DEFAULT '0' COMMENT '审核状态，0-待审核，1-审核未通过，2-审核通过',
    hi_online_status tinyint NOT NULL DEFAULT '1' COMMENT '0-下线，1-上线',
    hi_index_image_url varchar(256) NULL COMMENT '房屋主图片url',
    hi_utime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    hi_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (hi_house_id),
    KEY `hi_status` (hi_verify_status, hi_online_status),
    CONSTRAINT FOREIGN KEY (`hi_user_id`) REFERENCES `ih_user_profile` (`up_user_id`),
    CONSTRAINT FOREIGN KEY (`hi_area_id`) REFERENCES `ih_area_info` (`ai_area_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房屋信息表';


CREATE TABLE ih_house_facility (
    hf_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
    hf_house_id bigint unsigned NOT NULL COMMENT '房屋id',
    hf_facility_id int unsigned NOT NULL COMMENT '房屋设施',
    hf_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (hf_id),
    CONSTRAINT FOREIGN KEY (`hf_house_id`) REFERENCES `ih_house_info` (`hi_house_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房屋设施表';

CREATE TABLE ih_facility_catelog (
    fc_id int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
    fc_name varchar(32) NOT NULL COMMENT '设施名称',
    fc_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (fc_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='设施型录表';

CREATE TABLE ih_order_info (
    oi_order_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '订单id',
    oi_user_id bigint unsigned NOT NULL COMMENT '用户id',
    oi_house_id bigint unsigned NOT NULL COMMENT '房屋id',
    oi_begin_date date NOT NULL COMMENT '入住时间',
    oi_end_date date NOT NULL COMMENT '离开时间',
    oi_days int unsigned NOT NULL COMMENT '入住天数',
    oi_house_price int unsigned NOT NULL COMMENT '房屋单价，单位分',
    oi_amount int unsigned NOT NULL COMMENT '订单金额，单位分',
    oi_status tinyint NOT NULL DEFAULT '0' COMMENT '订单状态，0-待接单，1-待支付，2-已支付，3-待评价，4-已完成，5-已取消，6-拒接单',
    oi_comment text NULL COMMENT '订单评论',
    oi_utime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
    oi_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (oi_order_id),
    KEY `oi_status` (oi_status),
    CONSTRAINT FOREIGN KEY (`oi_user_id`) REFERENCES `ih_user_profile` (`up_user_id`),
    CONSTRAINT FOREIGN KEY (`oi_house_id`) REFERENCES `ih_house_info` (`hi_house_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表';

CREATE TABLE ih_house_image (
    hi_image_id bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '图片id',
    hi_house_id bigint unsigned NOT NULL COMMENT '房屋id',
    hi_url varchar(256) NOT NULL COMMENT '图片url',
    hi_ctime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    PRIMARY KEY (hi_image_id),
    CONSTRAINT FOREIGN KEY (hi_house_id) REFERENCES ih_house_info (hi_house_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='房屋图片表';

