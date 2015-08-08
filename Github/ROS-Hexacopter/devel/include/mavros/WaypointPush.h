// Generated by gencpp from file mavros/WaypointPush.msg
// DO NOT EDIT!


#ifndef MAVROS_MESSAGE_WAYPOINTPUSH_H
#define MAVROS_MESSAGE_WAYPOINTPUSH_H

#include <ros/service_traits.h>


#include <mavros/WaypointPushRequest.h>
#include <mavros/WaypointPushResponse.h>


namespace mavros
{

struct WaypointPush
{

typedef WaypointPushRequest Request;
typedef WaypointPushResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct WaypointPush
} // namespace mavros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::mavros::WaypointPush > {
  static const char* value()
  {
    return "2ee09985f8bc143dd5e9ab2eb6bfdea4";
  }

  static const char* value(const ::mavros::WaypointPush&) { return value(); }
};

template<>
struct DataType< ::mavros::WaypointPush > {
  static const char* value()
  {
    return "mavros/WaypointPush";
  }

  static const char* value(const ::mavros::WaypointPush&) { return value(); }
};


// service_traits::MD5Sum< ::mavros::WaypointPushRequest> should match 
// service_traits::MD5Sum< ::mavros::WaypointPush > 
template<>
struct MD5Sum< ::mavros::WaypointPushRequest>
{
  static const char* value()
  {
    return MD5Sum< ::mavros::WaypointPush >::value();
  }
  static const char* value(const ::mavros::WaypointPushRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::mavros::WaypointPushRequest> should match 
// service_traits::DataType< ::mavros::WaypointPush > 
template<>
struct DataType< ::mavros::WaypointPushRequest>
{
  static const char* value()
  {
    return DataType< ::mavros::WaypointPush >::value();
  }
  static const char* value(const ::mavros::WaypointPushRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::mavros::WaypointPushResponse> should match 
// service_traits::MD5Sum< ::mavros::WaypointPush > 
template<>
struct MD5Sum< ::mavros::WaypointPushResponse>
{
  static const char* value()
  {
    return MD5Sum< ::mavros::WaypointPush >::value();
  }
  static const char* value(const ::mavros::WaypointPushResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::mavros::WaypointPushResponse> should match 
// service_traits::DataType< ::mavros::WaypointPush > 
template<>
struct DataType< ::mavros::WaypointPushResponse>
{
  static const char* value()
  {
    return DataType< ::mavros::WaypointPush >::value();
  }
  static const char* value(const ::mavros::WaypointPushResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MAVROS_MESSAGE_WAYPOINTPUSH_H