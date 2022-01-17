cube(`Athlete`, {
  sql: `SELECT * FROM public.athlete`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [id, firstName, lastName]
    }
  },
  
  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primaryKey: true
    },
    
    sport: {
      sql: `sport`,
      type: `string`
    },
    
    year: {
      sql: `year`,
      type: `string`
    },
    
    firstName: {
      sql: `first_name`,
      type: `string`
    },
    
    lastName: {
      sql: `last_name`,
      type: `string`
    },
    
    grade: {
      sql: `grade`,
      type: `string`
    },
    
    hometown: {
      sql: `hometown`,
      type: `string`
    },
    
    highschool: {
      sql: `highschool`,
      type: `string`
    },
    
    link: {
      sql: `link`,
      type: `string`
    }
  },
  
  dataSource: `default`
});
