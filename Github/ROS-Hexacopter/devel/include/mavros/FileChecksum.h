// Generated by gencpp from file mavros/FileChecksum.msg
// DO NOT EDIT!


#ifndef MAVROS_MESSAGE_FILECHECKSUM_H
#define MAVROS_MESSAGE_FILECHECKSUM_H

#include <ros/service_traits.h>


#include <mavros/FileChecksumRequest.h>
#include <mavros/FileChecksumResponse.h>


namespace mavros
{

struct FileChecksum
{

typedef FileChecksumRequest Request;
typedef FileChecksumResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct FileChecksum
} // namespace mavros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::mavros::FileChecksum > {
  static const char* value()
  {
    return "c32158e17d9a1a1c682fe19adbd29fac";
  }

  static const char* value(const ::mavros::FileChecksum&) { return value(); }
};

template<>
struct DataType< ::mavros::FileChecksum > {
  static const char* value()
  {
    return "mavros/FileChecksum";
  }

  static const char* value(const ::mavros::FileChecksum&) { return value(); }
};


// service_traits::MD5Sum< ::mavros::FileChecksumRequest> should match 
// service_traits::MD5Sum< ::mavros::FileChecksum > 
template<>
struct MD5Sum< ::mavros::FileChecksumRequest>
{
  static const char* value()
  {
    return MD5Sum< ::mavros::FileChecksum >::value();
  }
  static const char* value(const ::mavros::FileChecksumRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::mavros::FileChecksumRequest> should match 
// service_traits::DataType< ::mavros::FileChecksum > 
template<>
struct DataType< ::mavros::FileChecksumRequest>
{
  static const char* value()
  {
    return DataType< ::mavros::FileChecksum >::value();
  }
  static const char* value(const ::mavros::FileChecksumRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::mavros::FileChecksumResponse> should match 
// service_traits::MD5Sum< ::mavros::FileChecksum > 
template<>
struct MD5Sum< ::mavros::FileChecksumResponse>
{
  static const char* value()
  {
    return MD5Sum< ::mavros::FileChecksum >::value();
  }
  static const char* value(const ::mavros::FileChecksumResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::mavros::FileChecksumResponse> should match 
// service_traits::DataType< ::mavros::FileChecksum > 
template<>
struct DataType< ::mavros::FileChecksumResponse>
{
  static const char* value()
  {
    return DataType< ::mavros::FileChecksum >::value();
  }
  static const char* value(const ::mavros::FileChecksumResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MAVROS_MESSAGE_FILECHECKSUM_H